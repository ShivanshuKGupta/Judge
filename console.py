class console:
    current_txt = ""

    @classmethod
    def print(cls, msg: str):
        msg = msg+'\t:'
        print('\b \b'*(len(cls.current_txt)+msg.count('\t')*8), end='')
        print(msg, end='')
        cls.current_txt = msg
