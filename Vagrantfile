Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 8192
    vb.cpus = 2
  end

  config.vm.provision "deps", type: "shell", path: "scripts/bionic-install-deps.sh"

  config.vm.provision "ndk", type: "shell", after: "deps", path: "scripts/download-ndk.sh"
end
