import boto3

# open connection to ec2
conn = get_ec2_conn()
# get a list of all instances
all_instances = conn.get_all_instances()
# get instances with filter of running + with tag `Name`
instances = conn.get_all_instances(filters={'tag-key': 'Name', 'instance-state-name': 'running'})
# make a list of filtered instances IDs `[i.id for i in instances]`
# Filter from all instances the instance that are not in the filtered list
instances_to_delete = [to_del for to_del in all_instances if to_del.id not in [i.id for i in instances]]
# run over your `instances_to_delete` list and terminate each one of them
for instance in instances_to_delete:
    conn.stop_instances(instance.id)


  