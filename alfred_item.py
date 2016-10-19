# author Ravi Hasija


class Item:
    def __init__(self, uid, title, arg, auto_complete, quick_look_url):
        self.uid = uid
        self.title = title
        self.subTitle = title
        self.arg = arg
        self.autoComplete = auto_complete
        self.quick_look_url = quick_look_url
