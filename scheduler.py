from google.cloud import scheduler_v1


secret_key_loc_ENV = "./scheduler-pubsub-key.json"
project_name_ENV = "fifth-boulder-362706"
location_name_ENV = "northamerica-northeast1"
time_zone = "Asia/Calcutta"
_topic_name_ = "daily-report-test-01"


def init_client(secret_key):
    """
    Initializes client instance.
    Requires location of client secret key (.json)
    """
    client = None

    try:
        client = scheduler_v1.CloudSchedulerClient.from_service_account_json(secret_key)
    except Exception as e:
        pass

    return client


def pubsub_target_make(topic_name, message, attribute_dict):
    """
    pubsub_target = {
            "topic_name": "projects/<project_name>/topics/<topic_name>",
            "data": message,
            "attributes": attribute_dict
            }
    """

    topic = "projects/{0}/topics/{1}".format(project_name_ENV, topic_name)
    pubsub_target = None

    try:
        pubsub_target = scheduler_v1.PubsubTarget(topic_name=topic, data=message.encode('utf-8'), attributes=attribute_dict)
    except Exception as e:
        print(e)

    return pubsub_target


def job_make(job_name, description, pubsub_target_instance, schedule):
    """
    job = {"name": "projects/<PROJECT_ID>/locations/<LOCATION_ID>/jobs/<JOB_ID>",
           "description": description,
           "pubsub_target": pubsub_target_instance,
           "schedule": schedule,
           "time_zone": time_zone
    }
    """
    job_name = "projects/{0}/locations/{1}/jobs/{2}".format(project_name_ENV, location_name_ENV, job_name)
    job = None

    try:
        job = scheduler_v1.Job(name=job_name, description=description, pubsub_target=pubsub_target_instance, schedule=schedule, time_zone=time_zone)
    except Exception as e:
        print(e)

    return job


def create_job(job_inst):
    location = "projects/{0}/locations/{1}".format(project_name_ENV,location_name_ENV)
    response = None
    client = None
    
    try:
        client = init_client(secret_key_loc_ENV)
        response = client.create_job(parent=location, job=job_inst)
    except Exception as e:
        print(e)
    
    print(response)
    return response


def read_job(job_name):
    client, request, response = None, None, None
    job_name = "projects/{0}/locations/{1}/jobs/{2}".format(project_name_ENV, location_name_ENV, job_name)

    try:
        client = init_client(secret_key_loc_ENV)
        request = scheduler_v1.GetJobRequest(name=job_name)
        
        response = client.get_job(request=request)
    
    except Exception as e:
        print(e)
    
    print(response)
    return response


def update_job(job_inst):
    client, request, response = None, None, None
    
    try:
        client = init_client(secret_key_loc_ENV)
        request = scheduler_v1.UpdateJobRequest(job=job_inst)

        response = client.update_job(request=request)
    
    except Exception as e:
        print(e)

    print(response)
    return(response)



def delete_job(job_name):
    client, request, response = None, None, None
    job_name = "projects/{0}/locations/{1}/jobs/{2}".format(project_name_ENV, location_name_ENV, job_name)

    try:
        client = init_client(secret_key_loc_ENV)
        request = scheduler_v1.DeleteJobRequest(name=job_name)
        
        response = client.delete_job(request=request)
    
    except Exception as e:
        print(e)
    
    print(response)
    return response


"""


# pubsub_target = pubsub_target_make(_topic_name_, "iiiiyyyaaaaa", {"k1":"v1","k2":"v2"})
# job = job_make("schedule-local-machine-01", "testing from my local machine", pubsub_target, "* * * * *")
# 
# create_job(job)

# read_job("schedule-local-machine-01")

# pubsub_target = pubsub_target_make(_topic_name_, "Yo, this is the update pubsub message", {"ky1":"vl1","ky2":"vl2"})
# job = job_make("schedule-local-machine-01", "testing update of job from my local machine", pubsub_target, "* * * * *")
# update_job(job)

# delete_job("schedule-local-machine-00")
# read_job("schedule-local-machine-00")


"""
