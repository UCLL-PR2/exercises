import inspect
import pytest
import filesystem


def if_class_exists(class_name):
    return pytest.mark.skipif(class_name not in dir(filesystem), reason=f'Skipped because {class_name} has not been defined')


def is_class_abstract(c):
    return inspect.isabstract(c)


def is_abstract_method(cls, method_name):
    return method_name in cls.__abstractmethods__


def has_property(cls, *, property_name, abstract=False):
    if not hasattr(cls, property_name):
        return False
    prop = getattr(cls, property_name)
    if type(prop) is not property:
        return False
    if prop.__isabstractmethod__ != abstract:
        return False
    return True


def has_method(cls, *, method_name, parameter_names=None, abstract=False):
    if parameter_names is None:
        parameter_names = []

    if not hasattr(cls, method_name):
        return False
    method = getattr(cls, method_name)
    if not inspect.isfunction(method):
        return False
    if abstract:
        if not is_abstract_method(cls, method_name):
            return False
    specs = inspect.getfullargspec(method)
    if specs.args != parameter_names:
        return False
    return True


def test_storage_device_class_is_defined():
    assert 'StorageDevice' in dir(filesystem), 'StorageDevice class has not been defined'


@if_class_exists('StorageDevice')
@pytest.mark.parametrize('property_name', [
    'total_block_count',
    'available_block_count',
    'used_block_count',
    'block_size',
])
def test_storage_device_properties(property_name):
    assert has_property(
        filesystem.StorageDevice,
        property_name=property_name
        ), f"StorageDevice must have property {property_name}"


@if_class_exists('StorageDevice')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'block_count', 'block_size'],
        'abstract': False,
    },
    {
        'method_name': 'allocate',
        'parameter_names': ['self', 'block_count'],
        'abstract': False,
    },
    {
        'method_name': 'free',
        'parameter_names': ['self', 'blocks'],
        'abstract': False,
    },
])
def test_storage_device_methods(kwargs):
    assert has_method(
        filesystem.StorageDevice,
        **kwargs), f"StorageDevice's method {kwargs['method_name']} is missing or incorrect"


def test_entity_class_is_defined():
    assert 'Entity' in dir(filesystem), 'Entity class has not been defined'


@if_class_exists('Entity')
def test_entity_class_is_abstract():
    assert is_class_abstract(filesystem.Entity)

@if_class_exists('Entity')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'name',
        'abstract': False,
    },
    {
        "property_name": 'size_in_blocks',
        'abstract': True,
    },
    {
        "property_name": 'size_in_bytes',
        'abstract': False,
    },
    {
        "property_name": 'storage',
        'abstract': False,
    },
])
def test_entity_properties(kwargs):
    assert has_property(filesystem.Entity, **kwargs), f"Entity's property {kwargs['property_name']} is missing or incorrect"


@if_class_exists('Entity')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'storage', 'name'],
        'abstract': False,
    },
    {
        'method_name': 'clear',
        'parameter_names': ['self'],
        'abstract': True,
    },
])
def test_entity_methods(kwargs):
    assert has_method(
        filesystem.Entity,
        **kwargs), f"Entity's method {kwargs['method_name']} is missing or incorrect"


def test_file_class_is_defined():
    assert 'File' in dir(filesystem), 'File class has not been defined'


@if_class_exists('File')
def test_file_class_is_not_abstract():
    assert not is_class_abstract(filesystem.File)


@if_class_exists('File')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'name',
        'abstract': False,
    },
    {
        "property_name": 'size_in_blocks',
        'abstract': False,
    },
    {
        "property_name": 'size_in_bytes',
        'abstract': False,
    },
    {
        "property_name": 'storage',
        'abstract': False,
    },
])
def test_file_properties(kwargs):
    assert has_property(filesystem.File, **kwargs), f"File's property {kwargs['property_name']} is missing or incorrect"


@if_class_exists('File')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'storage', 'name'],
        'abstract': False,
    },
    {
        'method_name': 'clear',
        'parameter_names': ['self'],
        'abstract': False,
    },
    {
        'method_name': 'grow',
        'parameter_names': ['self', 'block_count'],
        'abstract': False,
    },
])
def test_file_methods(kwargs):
    assert has_method(
        filesystem.File,
        **kwargs), f"File's method {kwargs['method_name']} is missing or incorrect"


def test_directory_class_is_defined():
    assert 'Directory' in dir(filesystem), 'Directory class has not been defined'


@if_class_exists('Directory')
def test_directory_class_is_not_abstract():
    assert not is_class_abstract(filesystem.Directory)


@if_class_exists('Directory')
@pytest.mark.parametrize('kwargs', [
    {
        "property_name": 'name',
        'abstract': False,
    },
    {
        "property_name": 'size_in_blocks',
        'abstract': False,
    },
    {
        "property_name": 'size_in_bytes',
        'abstract': False,
    },
    {
        "property_name": 'storage',
        'abstract': False,
    },
])
def test_directory_properties(kwargs):
    assert has_property(filesystem.Directory, **kwargs), f"Directory's property {kwargs['property_name']} is missing or incorrect"


@if_class_exists('Directory')
@pytest.mark.parametrize('kwargs', [
    {
        'method_name': '__init__',
        'parameter_names': ['self', 'storage', 'name'],
        'abstract': False,
    },
    {
        'method_name': 'clear',
        'parameter_names': ['self'],
        'abstract': False,
    },
    {
        'method_name': 'add',
        'parameter_names': ['self', 'entity'],
        'abstract': False,
    },
])
def test_directory_methods(kwargs):
    assert has_method(
        filesystem.Directory,
        **kwargs), f"Directory's method {kwargs['method_name']} is missing or incorrect"
