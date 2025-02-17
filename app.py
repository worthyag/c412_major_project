import os
import sys


def install_dependencies(os_type: str = "centos"):
    print("Checking and installing dependencies...")
    if os_type == "mac":
        pass

    elif os_type == "centos":
        os.system("yum -y install epel-release")
        os.system("yum -y update")
        os.system("yum -y install sysbench stress stress-ng iperf3")

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


def cpu_stress_test():
    print("Starting the 'CPU Stress' test...")  # change to log.
    # Run test
    os.system("stress --cpu 4 --timeout 60")


def mysql_stress_test():
    print("Starting the 'MySQL Stress' test...")  # change to log.
    # Run test
    # Prepare
    os.system(
        "sysbench --test=oltp --oltp-table-size=1000000 --mysql-db=test --mysql-user=root --mysql-password=password12- prepare"
    )

    # Benchmark
    os.system(
        "sysbench --test=oltp --oltp-table-size=1000000 --mysql-db=test --mysql-user=root --mysql-password=password12- --max-time=60 --oltp-read-only=on --max-requests=0 --num-threads=8 run"
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
