from sshpubkeys import SSHKey

pub_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDS4ZCRAuR7Gr0SS2B3XR3IYLcwrCVTSu9nzEDIBHxkVYM+zwO4SBXxECJaOZMI14hgYGa1KMGMqoVAtd72Te+Uwmu4iwGNWW5mheAGUMsYJHhUzTpKxcHqhmXCJI9ngbrPO6KoBVSmYQ1QkYBMI/E8jYBPIy8cfMJIeX7/TL8irTrfA3RS04l84ngSCOFipLLsBq4fbDVc6qbMF6Y4hGcknpOY5PbqX/nG2PdNJ68acT9K1IwqXmi9ZukX1yvpH4a1J4EkwbMyrvrV+3f5RYyHOJr+HL9PhDUWu04zxg2RYl75mbLFOA+kZ92YxF8DRMh6k37GD+VvA56Q+33owZl1"
ssh = SSHKey(pub_key)
ssh.parse()
print(ssh.hash_md5())
# MD5:c9:91:4f:48:43:2f:83:66:cc:22:d3:57:b2:69:40:7a