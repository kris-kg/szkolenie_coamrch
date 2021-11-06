class HelloMeta(type):

    def hello(class_):
        print("pozdrowienia z %s, pochodząej z metaklasy HelloMeta" %(type(class_())))

    def __call__(self,*args,**kwargs):
        class_ = type.__call__(self,*args)
        setattr(class_,"hello",self.hello)
        return class_

class ZwHello(object, metaclass=HelloMeta):
    def powitanie(self):
        self.hello()


gr = ZwHello()
gr.powitanie()