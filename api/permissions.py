from rest_framework import permissions

class TurnPermission(permissions.BasePermission):
    message= 'Artiq yerler doludur'
    def has_object_permission(self, request, view, obj):
        if obj.max_person  == obj.persons.count():
            self.message['errors'].clear()
            return False
        else:
            return True

