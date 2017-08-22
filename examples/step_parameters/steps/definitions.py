from behave import given, when, then

@given("I have a new {item} in my cart")
def i_have_an_item(context,item):
    print("I have bought an {}".format(item))

@when("I click on {button_to_click}")
def click_button(context,button_to_click):
    print("I have clicked on {}".format(button_to_click))

@then("I should see {txt}")
def _text_to_see(context,txt):
    print("I am seeing {}".format(txt))

@given("I start a call with {qty} participants")
def call_participant_count(context,qty):
    print("The call has {} participants".format(qty))
