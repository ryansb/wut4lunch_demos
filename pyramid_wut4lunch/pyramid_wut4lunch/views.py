from pyramid.view import view_config
import transaction
import pyramid.httpexceptions as exc
from formencode import Schema, validators
from pyramid_simpleform import Form
from pyramid_simpleform.renderers import FormRenderer

from pyramid_wut4lunch.models import DBSession, Lunch

class LunchSchema(Schema):
    submitter = validators.UnicodeString()
    food = validators.UnicodeString()

@view_config(route_name='home',
             renderer='templates/index.pt')
def home(request):
    lunches = DBSession.query(Lunch).all()
    form = Form(request, schema=LunchSchema())
    return {'lunches': lunches, 'form': FormRenderer(form)}


@view_config(route_name='newlunch',
             renderer='templates/index.pt',
             request_method='POST')
def newlunch(request):
    form = Form(request, schema=LunchSchema())
    if not form.validate:
        raise exc.HTTPBadRequest

    l = Lunch(
        submitter=request.POST.get('submitter', 'nobody'),
        food=request.POST.get('food', 'nothing'),
    )

    with transaction.manager:
        DBSession.add(l)

    raise exc.HTTPSeeOther('/')
