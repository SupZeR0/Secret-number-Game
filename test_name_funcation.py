from name_funcation import get_formatted_name

def test_first_last_name():
  formatted_name = get_formatted_name('abdo', 'shaker')
  assert formatted_name == "Abdo Shaker"

def test_first_last_middle_name():
  formatted_name = get_formatted_name('abdo','fathe','shaker')
  assert formatted_name == "Abdo Shaker Fathe"