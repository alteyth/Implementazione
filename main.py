from nanodevice import NanoDevice

if __name__ == "__main__":
    Controller = NanoDevice()

    Controller.connect()

    Controller.get_operation_mode()

    Controller.disconnect()
