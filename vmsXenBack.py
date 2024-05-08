#!/usr/bin/env python3
import XenAPI
import getpass

class XenServerManager:
    def __init__(self):
        self.session = XenAPI.Session("http://" + input("Ingresa la dirección IP del servidor XenServer: "))
        self.session.xenapi.login_with_password(input("Ingresa tu nombre de usuario: "), getpass.getpass("Ingresa tu contraseña: "))

    def __del__(self):
        self.session.xenapi.logout()

    def get_vm_ref_by_name(self, vm_name):
        vms = self.session.xenapi.VM.get_all()
        for vm_ref in vms:
            record = self.session.xenapi.VM.get_record(vm_ref)
            if record["name_label"] == vm_name:
                return vm_ref
        return None

    def list_vms(self):
        vms = self.session.xenapi.VM.get_all()
        for vm_ref in vms:
            record = self.session.xenapi.VM.get_record(vm_ref)
            print(f"Nombre: {record['name_label']} | UUID: {record['uuid']}")

def main():
    try:
        xen_manager = XenServerManager()
        xen_manager.list_vms()
    except XenAPI.Failure as e:
        print(f"Error XenAPI: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

