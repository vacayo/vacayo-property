import json
from django.utils.dateparse import parse_datetime
from django.views.generic.edit import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..services.property import PropertyService
from ..services.email import EmailService
from ..models.owner import Owner
from ..models.property import Property

property_service = PropertyService()
email_service = EmailService()


class AddressView(View):

    def get(self, request):
        address = request.GET.get('query')

        if not address:
            raise Exception('No address provided')

        addresses = property_service.geocode(address)

        return JsonResponse({
            'status': 'ok',
            'results': [{'value': v} for v in addresses]
        })


class PropertyView(View):

    def get(self, request):
        address = request.GET.get('address')

        if not address:
            raise Exception('No address provided')

        prop = property_service.lookup(address)

        return JsonResponse({
            'status': 'ok',
            'results': prop
        })


@method_decorator(csrf_exempt, name='dispatch')
class RegistrationView(View):

    def post(self, request):
        data = json.loads(request.body)
        owner_data = data.get('owner')
        property_data = data.get('property')
        
        owner, _ = Owner.objects.get_or_create(**owner_data)

        address = property_service.parse(property_data.get('address'))
        property_data['available_date'] = parse_datetime(property_data.get('available_date')).date()
        property, _ = Property.objects.get_or_create(
            address1=address.get('address1'),
            address2=address.get('address2'),
            city=address.get('city'),
            state=address.get('state'),
            zip_code=address.get('zip_code'),
            bedrooms=property_data.get('bedrooms'),
            bathrooms=property_data.get('bathrooms'),
            home_type=property_data.get('home_type'),
            home_size=property_data.get('home_size'),
            available_date=property_data.get('available_date'),
            last_rent=property_data.get('last_rent'),
        )

        owner.properties.add(property)

        try:
            email_service.send_registration_confirmation_email(
                to_email=owner.email,
                to_name=owner.first_name,
                address=address.get('address1'),
                quote=property_data.get('quote')
            )
        except Exception, e:
            pass

        return JsonResponse({
            'status': 'ok'
        })
