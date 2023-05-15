import os

def create_qos_policy():
    policy_name = input("Enter the policy name: ")
    executable_name = input("Enter the application executable name: ")
    bandwidth_limit = input("Enter the throttle rate (in Kbps): ") + "Kb"

    script_content = f"""
$policyName = "{policy_name}"
$executableName = "{executable_name}"
$bandwidthLimit = {bandwidth_limit}

# Create QoS policy
New-NetQosPolicy -Name $policyName -AppPathNameMatchCondition $executableName -ThrottleRateActionBitsPerSecond $bandwidthLimit
"""

    script_path = f"create_qos_policy_{policy_name}.ps1"
    if os.path.exists(script_path):
        print("A policy with the same name already exists. Remove it before creating another with the same name.")
        return
    with open(script_path, "w") as script_file:
        script_file.write(script_content)

    os.system(f"powershell.exe -ExecutionPolicy Bypass -File {script_path}")

def remove_qos_policy():
    policy_name = input("Enter the policy name to remove: ")

    script_content = f"""
$policyName = "{policy_name}"

# Remove the QoS policy by name
Remove-NetQosPolicy -Name $policyName
"""

    script_path = f"remove_qos_policy_{policy_name}.ps1"
    script_path0 = f"create_qos_policy_{policy_name}.ps1"

    with open(script_path, "w") as script_file:
        script_file.write(script_content)

    

    os.system(f"powershell.exe -ExecutionPolicy Bypass -File {script_path}")

    os.remove(script_path)
    if os.path.exists(script_path0):
        os.remove(script_path0)

def main():
    while True:
        action = input("Enter 'create' to create a QoS policy, 'remove' to remove a QoS policy, or 'exit' to quit: ")

        if action == "create":
            create_qos_policy()
        elif action == "remove":
            remove_qos_policy()
        elif action == "exit":
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
