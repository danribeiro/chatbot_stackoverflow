from unittest.mock import Mock

from behave import given, when, then
from test_controller import TestController


@given('a bot and update from server')
def step_impl(context):
    context.bot = Mock()
    context.update = Mock()
    context.dispatcher = Mock()
    # context.dbhandler = Mock()
    # context.dbhandler.add_user.return_value = context.user
    context.test_controller = TestController(dispatcher=context.dispatcher)


@when('user send /search django python')
def step_impl(context):
    args = ['django', 'python']
    data = context.test_controller.search_tags(bot=context.bot, update=context.update, args=args)
    assert data is not None


@then('return question list')
def step_impl(context):
    args = ['django', 'python']
    data = context.test_controller.search_tags(bot=context.bot, update=context.update, args=args)
    assert data['items'].__len__() > 0