import pytest
from django.core.files import File
from rest_framework.test import APIClient
from core import models as _m

# Create your tests here.
PRODUCT_NAME = 'test_product_name'
PRODUCT_DESCRIPTION = 'test_product_description'
VARIANT_NAME = 'test_variant_name'
VARIANT_SIZE = '1.3m * 1.3m * 0.8m'
VARIANT_COLOR = 'red'
FIXTURE_PATH = 'core/fixtures/'
IMAGE_FILE = 'WechatIMG10.jpeg'


class TestBaseView:

    @pytest.fixture
    def client(self):
        client = APIClient()
        return client

    @pytest.fixture
    def product(self):
        product_data = {
            'name': PRODUCT_NAME,
            'description': None,
            'logo': None,
        }
        product_obj = _m.Products.objects.create(**product_data)
        with open(f'{FIXTURE_PATH}{IMAGE_FILE}', 'rb') as f:
            product_obj.logo.save(IMAGE_FILE, File(f))
        return product_obj

    @pytest.fixture
    def variant(self, product):
        variant_data = {
            'name': VARIANT_NAME,
            'size': None,
            'color': None,
            'product_id': product.id,
        }
        variant_obj = _m.Variants.objects.create(**variant_data)
        return variant_obj

    @pytest.fixture
    def image(self):
        image_data = {
            'Url': None,
        }
        image_obj = _m.Images.objects.create(**image_data)
        with open(f'{FIXTURE_PATH}{IMAGE_FILE}', 'rb') as f:
            image_obj.Url.save(IMAGE_FILE, File(f))
        return image_obj

    @pytest.mark.django_db
    def clean_up(self):
        """_summary_
        This function is use for clean up the upload file in the folder.
        """
        _m.Images.objects.all().delete()
        assert _m.Images.objects.all().count() == 0
        _m.Variants.objects.all().delete()
        assert _m.Variants.objects.all().count() == 0
        _m.Products.objects.all().delete()
        assert _m.Products.objects.all().count() == 0


class TestProductView(TestBaseView):
    VIEW_URL = '/products/'

    @pytest.mark.django_db
    def test_get_empty_response(self, client):
        response = client.get(f'{self.VIEW_URL}')
        assert response.json()['results'] == []

    @pytest.mark.django_db
    def test_get_one_result_by_id(self, client, product):
        response = client.get(f'{self.VIEW_URL}{product.id}/')
        assert response.status_code == 200
        result = response.json()
        assert result['id'] == product.id
        assert result['name'] == product.name
        self.clean_up()

    @pytest.mark.django_db
    def test_create_product_data(self, client):
        with open(f'{FIXTURE_PATH}{IMAGE_FILE}', 'rb') as f:
            product_data = {
                'name': PRODUCT_NAME,
                'description': PRODUCT_DESCRIPTION,
                'logo': f,
            }
            response = client.post(f'{self.VIEW_URL}', data=product_data)
        assert response.status_code == 201
        result = response.json()
        assert result['name'] == PRODUCT_NAME
        assert result['description'] == PRODUCT_DESCRIPTION
        self.clean_up()

    @pytest.mark.django_db
    def test_update_product_data(self, client, product):
        with open(f'{FIXTURE_PATH}{IMAGE_FILE}', 'rb') as f:
            product_data = {
                'name': PRODUCT_NAME,
                'description': PRODUCT_DESCRIPTION,
                'logo': f,
            }
            response = client.put(f'{self.VIEW_URL}{product.id}/', data=product_data)
        assert response.status_code == 200
        result = response.json()
        assert result['id'] == product.id
        assert result['name'] == PRODUCT_NAME
        assert result['description'] == PRODUCT_DESCRIPTION
        self.clean_up()

    @pytest.mark.django_db
    def test_delete_product_data(self, client, product):
        assert _m.Products.objects.all().count() == 1
        response = client.delete(f'{self.VIEW_URL}{product.id}/')
        assert response.status_code == 204
        assert _m.Products.objects.all().count() == 0


class TestVariantView(TestBaseView):
    VIEW_URL = '/variants/'

    @pytest.mark.django_db
    def test_get_empty_response(self, client):
        response = client.get(f'{self.VIEW_URL}')
        assert response.json()['results'] == []

    @pytest.mark.django_db
    def test_get_one_result_by_id(self, client, variant):
        response = client.get(f'{self.VIEW_URL}{variant.id}/')
        assert response.status_code == 200
        result = response.json()
        assert result['id'] == variant.id
        assert result['name'] == variant.name
        assert result['product'] == variant.product.id
        self.clean_up()

    @pytest.mark.django_db
    def test_create_variant_data(self, client, product):
        variant_data = {
            'name': VARIANT_NAME,
            'size': VARIANT_SIZE,
            'color': VARIANT_COLOR,
            'product': product.id,
        }
        response = client.post(f'{self.VIEW_URL}', data=variant_data)
        assert response.status_code == 201
        result = response.json()
        assert result['name'] == VARIANT_NAME
        assert result['size'] == VARIANT_SIZE
        assert result['color'] == VARIANT_COLOR
        assert result['product'] == product.id
        self.clean_up()

    @pytest.mark.django_db
    def test_update_variant_data(self, client, product, variant):
        variant_data = {
            'name': VARIANT_NAME,
            'size': VARIANT_SIZE,
            'color': VARIANT_COLOR,
            'product': product.id,
        }
        response = client.put(f'{self.VIEW_URL}{variant.id}/', data=variant_data)
        assert response.status_code == 200
        result = response.json()
        assert result['id'] == variant.id
        assert result['size'] == VARIANT_SIZE
        assert result['color'] == VARIANT_COLOR
        assert result['product'] == product.id
        self.clean_up()

    @pytest.mark.django_db
    def test_delete_variant_data(self, client, variant):
        assert _m.Variants.objects.all().count() == 1
        response = client.delete(f'{self.VIEW_URL}{variant.id}/')
        assert response.status_code == 204
        assert _m.Variants.objects.all().count() == 0
        self.clean_up()


class TestImageView(TestBaseView):
    VIEW_URL = '/images/'

    @pytest.mark.django_db
    def test_get_empty_response(self, client):
        response = client.get(f'{self.VIEW_URL}')
        assert response.json()['results'] == []

    @pytest.mark.django_db
    def test_get_one_result_by_id(self, client, image):
        response = client.get(f'{self.VIEW_URL}{image.id}/')
        assert response.status_code == 200
        result = response.json()
        assert result['id'] == image.id
        self.clean_up()

    @pytest.mark.django_db
    def test_create_image_data(self, client):
        with open(f'{FIXTURE_PATH}{IMAGE_FILE}', 'rb') as f:
            image_data = {
                'Url': f,
            }
            response = client.post(f'{self.VIEW_URL}', data=image_data)
        assert response.status_code == 201
        self.clean_up()

    @pytest.mark.django_db
    def test_update_image_data(self, client, product, variant, image):
        with open(f'{FIXTURE_PATH}{IMAGE_FILE}', 'rb') as f:
            image_data = {
                'Url': f,
                'product': product.id,
                'variant': variant.id
            }
            response = client.put(f'{self.VIEW_URL}{image.id}/', data=image_data)
        assert response.status_code == 200
        result = response.json()
        assert result['id'] == image.id
        assert result['product'] == product.id
        assert result['variant'] == variant.id
        self.clean_up()

    @pytest.mark.django_db
    def test_delete_image_data(self, client, image):
        assert _m.Images.objects.all().count() == 1
        response = client.delete(f'{self.VIEW_URL}{image.id}/')
        assert response.status_code == 204
        assert _m.Images.objects.all().count() == 0
        self.clean_up()
