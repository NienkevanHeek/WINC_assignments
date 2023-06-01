# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

def greet(name = "", greeting_template = 'Hello, <name>!'):
   if name:
      return greeting_template.replace('<name>', name)
   else:
      return greeting_template

def force(mass, body = "earth"):
   planetary_gravity_dict = {"mercury": 3.7, "venus": 8.9, "earth": 9.8, "moon": 1.6, "mars": 3.7, "jupiter": 23.1, "saturn": 9.0, "uranus": 8.7, "neptune": 11.0, "pluto": 0.7}
   force_calc = mass * round(planetary_gravity_dict[body], 1)
   return force_calc

def pull(m1, m2, d):
   pull_calc = 6.674*10**-11*((m1*m2)/d**2)
   return pull_calc 

print(greet())
print(force(mass = 6))
print(pull(m1 = 0.330, m2 = 4.87, d=7))
