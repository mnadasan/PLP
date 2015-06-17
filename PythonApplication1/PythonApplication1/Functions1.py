print('hello world')

def greet(name):
    return "hello " + name

greet_someone = greet
print(greet_someone("John"))

#decorators
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

def get_my_text(name):
   return "look at {0} how nice he codes".format(name)

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

my_get_text = p_decorate(get_text)

print(my_get_text("John"))
print(p_decorate(get_my_text)("MM"))
