# LION - Reunion, Madagascar
# SAFE - Cochin (India), Melkbosstrand (Using Nelspruit instead, South Africa), Mtunzini (Using Durban instead, South Africa), Penang (Malaysia), Reunion
# MARS - Port Mathurin (Rodrigues)

# dictionary holding speedtest servers and their respective codes
server_dict = {'LION': {'reunion': 24492, 'madagascar': 7755},
               'SAFE': {'india': 24682, 'south_africa_1': 19027, 'south_africa_2': 1285, 'malaysia': 12544},
               'MARS': {'rodrigues': 27454}
               }

# launch a process for initiating speedtest
# must install official speedtest-cli from Ookla (https://www.speedtest.net/apps/cli)


def run_speedtest(server_code, country):

    import subprocess
    from datetime import datetime

    # Open JSON file to write stdout obtained from subprocess. File name based on country name and datetime test was run.
    shell_file = open(
        f'./response/response_{country}_{str(datetime.now())}.json', 'w')

    # Run speedtest-cli from subprocess
    subprocess.run(["speedtest", "-s", str(server_code), "-f",
                    "json-pretty", "-P", "8"], stdout=shell_file)
    # Close file
    shell_file.close()


def main(server_list):
    # Iterate on server_dict. Unpack first level key-value pairs
    for cable, country in server_list.items():
        # print(cable)

        # Iterate on server_dict. Unpack second level key-value pairs.
        for server in country:
            # print(server)
            # Assign country name to variable
            server_country = server
            # print(country[server])
            # Assign server code to variable
            server_code = country[server]

            # Call run_speedtest function. Pass server code and country name.
            run_speedtest(server_code, server_country)


if __name__ == "__main__":
    # Run main. Pass in dictionary of servers.
    main(server_dict)
