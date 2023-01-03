from devices import Firewall, Loadbalancer, Switch
# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Create a LoadBalancer instance 
loadbalancer_01 = Loadbalancer("Dummy") 
# Configure it 
loadbalancer_01.configure_Loadbalancer() 
# Create a LoadBalancer instance 
loadbalancer_02 = Loadbalancer("Dummy")
# Verify a load
loadbalancer_02.calculate_Load("dummy data")

# Create a LoadBalancer instance 
Switch_01 = Switch("Dummy") 
# Configure it 
Switch_01.configure_Switch() 
# Create a LoadBalancer instance 
Switch_02 = Switch("Dummy")
# Verify a load
Switch_02.calculate_bandwidth("dummy data")