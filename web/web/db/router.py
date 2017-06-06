class router(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'manager':
            return 'manager'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'manager':
            return 'manager'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'manager' and obj2._meta.app_label == 'manager':
            return True
        elif 'manager' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False