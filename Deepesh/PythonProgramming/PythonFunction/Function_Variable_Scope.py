"""
local variable : When we define any variable inside the function, then it is called local
                variable. the scope of local variable is limited the function only
global variable:  The variable we declare outside the function, then it is called global variable
                all function inside the module can use the global variable
nonlocal variable : nonlocal variable is available for all the child function of outer function
                   -> If we want to change the value of global and nonlocal variable inside
                   function, we have to user keyword call global var_x and nonlocal var_y
"""

# global variable
var_p = 70

def function1():
    print("------- function1 --------------")
    var_q = 80 # local variable
    print("global variable var_p:", var_p)
    print("local variable var_q:", var_q)

def function2():
    global var_p
    print("------- function2 --------------")
    var_r = 90 # local variable
    var_p = 500
    print("global variable var_p:", var_p)
    print("local variable var_r:", var_r)


function1()
function2()
function1()


print("_"*40)
###################################################
var_x = 100 # global variable

def outer():
    var_y = 200 # nonlocal variable

    def fun1():
        global var_x
        nonlocal var_y
        var_z = 300 # local variable
        var_x = 700
        var_y = 800
        print("________fun1_______")
        print("global var_x :", var_x)
        print("nonlocal variable, var_y :", var_y)
        print("local variable var_z :", var_z)

    def fun2():
        var_w = 500 # local variable
        print("________fun2_______")
        print("global var_x :", var_x)
        print("nonlocal variable, var_y :", var_y)
        print("local variable var_w :", var_w)


    fun1()
    fun2()

outer()
