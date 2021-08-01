# **Automating Node Configuration with OOB Licensing Enabled**

## Follow the below procedures in order to license the Virtual Machine

1. **Connect node IPMI ports to VLAN53 Ports on the DELL EMC S4112-T Series Switch**

2. **Ensure the Master Laptop is connected to the switch as well**

3. **There are three playbooks that can be used, depending on the required configuration of the nodes**
    >- **`/opt/cure/ansible_main/automate_bios_RHV.yml`**
        - This playbook is used for configuring the Node BIOS per RHV Node requirements.
        
    >- **`/opt/cure/ansible_main/automate_bios_BAREMETAL.yml`**
        - This playbook is used for configuring the Node BIOS per Security Onion requirements.

    >- **`/opt/cure/ansible_main/baremetal_iso_install.yml`**
        - This playbook is used for automating the mounting and installation of an ISO image (i.e. Security Onion).

4. **The playbooks can be called by running the `./run.py` script**
    > **`./run.py`**

    > EXAMPLE: **`upload license http://10.59.51.2/redseal.lic`**

5. **Verify the license is active:**
    > **`show license`**

6. **Start the services (TAKES 5-7 MINS)**
    > **`startup server`**

7. **Check the status of the services:**
    > **`status server`** ( the last service will not start, purposely )