#pi='3.14'-->Not supposed to be a string
#pie.diameter=55.4-->invalid variable name
#should be /2 instead of //2
#After pi, it is supposed too be * instead of **
#circumference-msg-->invalid variable name

pi = 3.14
pie_diameter = 55.4
pie_radius = pie_diameter/2
circumference = 2*pi*pie_radius
circumference_msg="Jimmy's pie has a circumference:"
print(circumference_msg,circumference) 