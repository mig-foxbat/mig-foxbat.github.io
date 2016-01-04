




##### Docker in a Nutshell

Docker is to Linux what Virtualenv is to Python. As opposed to Hardware Emulation provided by VMs Docker provides OS Emulation but only limited to Linux. To help understand Docker we will have to first over simplify what is Linux and Linux Distros.

###### Linux stripped down

	Linux operating system or any operating system for that matter is just a Kernel and a bunch of binaries like shell,grep,sed etc that operates on top of the former. What the Linux Distros are different ways the Kernel and the binaries are packaged together as a single product. Each Linux distribution shares same Linux Kernel but what makes them different are the binary packages that comes along with ths OS and the file system layout of these binaries. 

###### Docker vs VM

	Virtual machines have an in-efficient way to spawn new instances. It Emulates an entire hardware and in this emulated hardware the entire Operating System (Kernel + Binaries) is loaded. How Docker trumps VMs is that they re-uses the Host's Kernel and only has to provide the binaries to be loaded for OS virtualization. The catch here is that since the Host's Kernel is reused you can only spawn Linux instances and the host will always have to be a Linux instance.

####### What makes Docker tick

	Though Docker has revolutionized how applications are deployed/run/tested, this has been made possible because of few evolutionary features of Linux. I listed few of the important ones here.

	1) chroot:
	   chroot changes the root of the file system visible to a process to a given directory. This is something widely used in FTP services. Say if you a Linux server hosting FTP/SFTP service and if user FTPs into the box, the chroot for that session is set to the user's home directory. This way the user has no way to switch to the real root directory or any other directory outside his home directory. ie `cd /` would land him into his home directory.

	2) UFS (Union File System):
		So as explained earlier, docker is a collection of binaries without the kernel.  






