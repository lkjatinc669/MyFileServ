# MyFileServ - A File Management and Streaming Server

MyFileServ is a Flask-based website server designed to provide a simple and secure solution for users within a local area network (LAN) to upload, store, and access files from a common computer. Users can create accounts with usernames and passwords to access their personal storage space, where they can upload files of any type and size without limitations. Additionally, there is a shared space accessible to all users, facilitating collaborative file sharing and storage.

## Features
1. User Authentication: Users create accounts with usernames and passwords for secure access to their personal storage space.
1. File Uploads: Users can upload files of any type and size to their personal storage space, with no limitations on file size.
1. Storage Management: Files are stored in a directory-based system, with each user having their own directory for personal storage.
1. Access Control: Uploaded files are accessible only to the user who uploaded them, ensuring privacy and security. Users can share files in the shared space, accessible to all users but only deletable by the uploader or admin.
1. Shared Space: A common user directory allows all users to view and access shared files, facilitating collaborative file sharing and storage.
1. User Interface: The user interface is designed to be easy to use and intuitive, providing a seamless experience for users to navigate and manage their files.
1. Data Security: Data is stored locally within the network, with multiple layers of security including network security, operating system security, and application security to protect user information.
1. Scalability: MyFileServ is designed to accommodate up to 10 users with 1-8 TB of storage space, with the flexibility to scale up by adding multiple HDDs or SSDs as needed in the future.

## Hardware Requirements:

1. **Server Computer:**
   - Minimum RAM: 4GB (8GB recommended)
   - Processor: Dual-core CPU or higher
   - Storage: Sufficient storage capacity to accommodate user files (1-8TB recommended)
   - Network Interface: Ethernet connection for LAN connectivity
   
2. **Storage Devices (Optional for Scalability):**
   - Additional Hard Disk Drives (HDDs) or Solid State Drives (SSDs) for expanding storage capacity as needed
   
3. **Network Equipment:**
   - Router or switch for LAN connectivity