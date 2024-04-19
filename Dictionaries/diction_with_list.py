ec2_instance_info =[
    {
        "id": "ec2-instance-001",
        "type": "t2.micro"
    },
    {
        "id": "ec2-instance-002",
        "type": "t3.medium"
    },
    {
        "id": "ec2-instance-003", 
        "type": "t2.xlarge"
    }
]

print(ec2_instance_info[1]["type"])
print(ec2_instance_info[2]["id"])