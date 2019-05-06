#import hashlib
#import time
#from pyfingerprint.pyfingerprint import PyFingerprint

def main_menu():
    print("----------------------")
    print("---     SLIIT      ---")
    print("----------------------")
    print("1. Enroll Students   -")
    print("2. Mark Attendance   -")
    print("3. Delete Student    -")
    print("4. Quit              -")
    print("----------------------")
    while True:
        try:
            select = int(input("Enter choice: "))
            if select == 1:
                enroll_stud()
                break
            elif select == 2:
                mark_stud()
                break
            elif select == 3:
                delete_stud()
                break
            elif select == 4:
                break
            else:
                print("Invalid choice. Enter 1-4: ")
                main_menu()
        except ValueError:
            print("Invalid choice. Enter 1-4: ")
    exit

# Enroll Students


def enroll_stud():
    print("Enroll Students")
    in_sensor()
    try:
        print('Waiting for finger...')
        while (f.readImage() == False):
            pass
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        if (positionNumber >= 0):
            print('Template already exists at position #' + str(positionNumber))
            exit(0)
        print('Remove finger...')
        time.sleep(2)
        print('Waiting for same finger again...')
        while (f.readImage() == False):
            pass
        f.convertImage(0x02)
        if (f.compareCharacteristics() == 0):
            raise Exception('Fingers do not match')
        f.createTemplate()
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
    main_menu()

# Mark Attendance
def mark_stud():
    print("Mark Attendance")
    in_sensor()
    try:
        print('Waiting for finger...')
        while ( f.readImage() == False ):
            pass
        f.convertImage(0x01)
        result = f.searchTemplate()
        positionNumber = result[0]
        accuracyScore = result[1]
        if ( positionNumber == -1 ):
            print('No match found!')
            exit(0)
        else:
            print('Found template at position #' + str(positionNumber))
            print('The accuracy score is: ' + str(accuracyScore))
        f.loadTemplate(positionNumber, 0x01)
        characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')
        print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
    main_menu()


# Delete Students
def delete_stud():
    print("Delete Student")
    in_sensor()
    try:
        positionNumber = input('Please enter the template position you want to delete: ')
        positionNumber = int(positionNumber)
        if ( f.deleteTemplate(positionNumber) == True ):
            print('Template deleted!')
    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
    main_menu()


# Initialize Sensor
def in_sensor():
    try:
        f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
        if (f.verifyPassword() == False):
            raise ValueError('The given fingerprint sensor password is wrong!')
    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    print('Currently used templates: ' + str(f.getTemplateCount()) +
        '/' + str(f.getStorageCapacity()))

# Main Routin
main_menu()
