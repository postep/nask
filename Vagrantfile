# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: "echo Hello"
  config.vm.define "serwer" do |serwer|
    serwer.vm.box = "debian/stretch64"
    serwer.vm.host_name = "serwer"
    serwer.vm.network "public_network", ip: "20.0.0.1/24"
    serwer.vm.provision "shell", inline: "sudo ip route add 10.0.0.0/24 via 20.0.0.4 dev eth1"
    serwer.vm.provision "shell", inline: "sudo apt update"
    serwer.vm.provision "shell", inline: "sudo apt install python3-apscheduler python3-scipy python3-matplotlib --assume-yes"
    serwer.vm.provision "shell", inline: "sudo python3 /vagrant/server.py &"
  end

  config.vm.define "klient" do |klient|
    klient.vm.box = "debian/stretch64"
    klient.vm.host_name = "klient"
    klient.vm.network "public_network", ip: "10.0.0.5/24"
    klient.vm.provision "shell", inline: "sudo ip route add 20.0.0.0/24 via 10.0.0.4 dev eth1"
    klient.vm.provision "shell", inline: "sudo apt update"
    klient.vm.provision "shell", inline: "sudo apt install python3-apscheduler python3-scipy python3-matplotlib --assume-yes"
    klient.vm.provision "shell", inline: "sudo python3 /vagrant/client.py &"
  end

  config.vm.define "router" do |router|
    router.vm.box = "debian/stretch64"
    router.vm.host_name = "router"
    router.vm.network "public_network", ip: "20.0.0.4/24"
    router.vm.network "public_network", ip: "10.0.0.4/24"
    router.vm.provision "shell", inline: "sysctl -w net.ipv4.ip_forward=1"
    router.vm.provision "shell", inline: "sudo apt update"
    router.vm.provision "shell", inline: "export DEBIAN_FRONTEND=noninteractive; apt-get -yq install snort"
    router.vm.provision "shell", inline: "sudo cp /vagrant/local.rules /etc/snort/rules/local.rules"
    router.vm.provision "shell", path: "mongo_install.bash"
    router.vm.provision "shell", inline: "sudo snort -q -A console -k none -c /etc/snort/snort.conf -i eth1 | sudo python3 /vagrant/security.py &"
  end
  
  # config.vm.define "snort" do |snort|
  #   snort.vm.box = "debian/stretch64"
  #   snort.vm.network "public_network", ip: "20.0.0.2/24"
  #   snort.vm.provision "shell", inline: "sudo ip route add 10.0.0.0/24 via 20.0.0.4 dev eth1"
  #   snort.vm.host_name = "snort"
  # end

  config.vm.define "zaklocenie" do |zaklocenie|
    zaklocenie.vm.box = "debian/stretch64"
    zaklocenie.vm.host_name = "zaklocenie"
    zaklocenie.vm.network "public_network", ip: "10.0.0.1/24"
    zaklocenie.vm.provision "shell", inline: "sudo ip route add 20.0.0.0/24 via 10.0.0.4 dev eth1"
    zaklocenie.vm.provision "shell", inline: "sudo apt update"
    zaklocenie.vm.provision "shell", inline: "sudo python3 /vagrant/client.py &"
  end

  # config.vm.define "db" do |db|
  #   db.vm.box = "debian/stretch64"
  #   db.vm.host_name = "db"
  #   db.vm.network "public_network", ip: "20.0.0.3/24"
  #   db.vm.provision "shell", path: "mongo_install.bash"
  # end

  config.vm.provider "virtualbox" do |v|
    v.memory = 3072
    v.cpus = 2
  end
end

  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  # config.vm.network "forwarded_port", guest: 80, host: 8080

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
  # SHELL
