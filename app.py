import os
import sys


def install_dependencies(os_type: str = "centos"):
    print("Checking and installing dependencies...")
    if os_type == "mac":
        print("Currently still working through!")

    elif os_type == "centos":
        print("Installing epel-release...")
        os.system("dnf install -y epel-release")
        os.system("dnf clean all && sudo dnf makecache")

        print("Installing stress and stress-ng...")
        os.system("dnf install -y stress stress-ng")

        print("Installing iperf3...")
        os.system("dnf install -y iperf3")

        # Installing mysqlslap (it is a built-in MySQL tool).
        print("Installing mysqlslap...")
        os.system("dnf install -y mysql mysql-server")
        # Starting the service on boot and starting it now.
        os.system("systemctl enable --now mysqld")

        # Verify install
        os.system(
            """
            stress --version;
            stress-ng --version;
            iperf3 --version;
            mysql --version;
            """
        )

    else:
        print("OS system not available!")


def memory_stress_test():
    print("Starting the 'Memory Stress' test...")  # change to log.
    # Run test
    os.system("stress --vm 2 --vm-bytes 1G --timeout 60")


def disk_stress_test():
    print("Starting the 'Disk Stress' test...")  # change to log.
    # Run test
    os.system("stress-ng --hdd 2 --hdd-bytes 2G --timeout 60")


def network_stress_test():
    print("Starting the 'Network Stress' test...")  # change to log.
    # Run test
    os.system("iperf3 -s &")
    print("Run 'iperf3 -c <server-ip>' from another machine to test.")


def cpu_stress_test():
    print("Starting the 'CPU Stress' test...")  # change to log.
    # Run test
    os.system("stress --cpu 4 --timeout 60")


def mysql_stress_test():
    print("Starting the 'MySQL Stress' test...")  # change to log.
    # Run test
    os.system(
        """mysqlslap --user=root --password=password12- --concurrency=10 --iterations=10 
        --create-schema=test --query='SELECT * FROM my_table;' --verbose"""
    )


def goodbye():
    print("Exiting...")
    sys.exit(0)


def main():
    install_dependencies("centos")

    while True:
        print(
            "\n------------- Stress Testing Menu -------------\n",
            "===============================================\n",
            "1. Memory Stress Testing\n",
            "2. Disk Stress Testing\n",
            "3. Network Stress Testing\n",
            "4. CPU Stress Testing\n",
            "5. MySQL Stress Testing\n",
            "6. Exit\n",
            "Enter the number corresponding to the test you would like to run.\n"
        )

        try:
            userSelection = int(input("> "))
        except ValueError:
            print("You must enter a number.")
            goodbye()

        if userSelection == 1:
            memory_stress_test()
        elif userSelection == 2:
            disk_stress_test()
        elif userSelection == 3:
            network_stress_test()
        elif userSelection == 4:
            cpu_stress_test()
        elif userSelection == 5:
            mysql_stress_test()
        elif userSelection == 6:
            goodbye()
        else:
            print("Invalid selection.")


main()
