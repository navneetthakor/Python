
isExceptionThrown = True

try:
    x = "navneet"

    try:
        if(isExceptionThrown): raise Exception("bad writting")
    
    except Exception as ex:
        print("Internal exception")
        raise Exception(ex)
    
    else:
        print("Internal else block")

    finally:
        print("Internal finally block")

except IOError as ex:
    print('IOError exception',ex)

except (SystemError,SyntaxError) as ex:
    print("Grouped exceptions", ex)

except Exception as ex: # this generic exception block must be place after all the other exception blocks
    print('Generic exception',ex)

else:   # execute if no exceptions will thrown
    print("No exception was thrown")

finally:
    print("Will always executed regarless of exception is raised or not")