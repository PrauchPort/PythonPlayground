class Smartphone(object):

    max_input_voltage = 5

    @classmethod
    def outcome(cls, input_voltage):
        if input_voltage > cls.max_input_voltage:
            print("Input voltage: {}V -- BURNING!!".format(input_voltage))
        else:
            print("Input voltage: {}V -- Charging...".format(input_voltage))

    def charge(self, input_voltage):
        """ Charge the phone with the given input voltage. """
        self.outcome(input_voltage)


class Socket(object):
    output_voltage = None


class EUSocket(Socket):
    output_voltage = 230


class USSocket(Socket):
    output_voltage = 120


class EUAdapter(object):
    """EUAdapter encapsulates client (Smartphone) and supplier (EUSocket)."""
    input_voltage = EUSocket.output_voltage
    output_voltage = Smartphone.max_input_voltage


class CannotTransformVoltageException(Exception):
    pass


class SmartphoneAdapter(Smartphone, Socket):

    @classmethod
    def transform_voltage(cls, input_voltage):
        if input_voltage == cls.output_voltage:
            return cls.max_input_voltage
        else:
            raise CannotTransformVoltageException("Cannot transform {0}--{1}V. This adapter transforms{2}--{1}V".format
                                                  (input_voltage, cls.max_input_voltage, cls.output_voltage))

    @classmethod
    def charge(cls, input_voltage):
        try:
            voltage = cls.transform_voltage(input_voltage)
            cls.outcome(voltage)
        except CannotTransformVoltageException as e:
            print(e)


class SmartphoneEUAdapter(SmartphoneAdapter, EUSocket):
    pass


class SmartphoneUSAdapter(SmartphoneAdapter, USSocket):
    pass


if __name__ == '__main__':
    # smartphone = Smartphone()
    # smartphone.charge(USSocket.output_voltage)
    # smartphone.charge(EUAdapter.output_voltage)

    seua = SmartphoneEUAdapter()
    seua.charge(EUSocket.output_voltage)
    susa = SmartphoneUSAdapter()
    seua.charge(USSocket.output_voltage)
