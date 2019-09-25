from hypethesis import given, settings

@given(integers())
@settings(max_examples=500)
def test_this(x):
    pass