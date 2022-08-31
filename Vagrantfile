# Copyright (c) Meta Platforms, Inc. and affiliates.

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 8192
    vb.cpus = 2
  end

  config.vm.provision "deps", type: "shell", path: "scripts/jammy-install-deps.sh"

  config.vm.provision "ndk", type: "shell", after: "deps" do |s|
    s.path = "scripts/download-ndk.sh"
    s.args = ["/opt/ndk"]
  end
end
