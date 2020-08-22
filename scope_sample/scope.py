def check_scope():
    def do_local():
        test="local test"
    def do_non_local():
        nonlocal test
        test="non local test"
    def do_global():
        global test
        test="global test"
    test="default test"
    do_local()
    print("Test value after do local:",test)
    do_non_local()
    print("test value after non local:",test)
    do_global()
    print("test value after global :",test)
check_scope()
print("test value after main :",test)
