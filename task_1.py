from queue import Queue
import threading
import random
import sys
import time


queue = Queue()
request_id = 1
stop_event = threading.Event()


def generate_request():
    global request_id

    new_request = {
        "status": "open",
        "id": request_id
    }
    queue.put(new_request)
    print(f"Request #{request_id} created!")
    request_id += 1


def process_request():
    if not queue.empty():
        request = queue.get()
        time.sleep(2)
        request["status"] = "closed"
        print(f"Request #{request['id']} processed successfully!")
    else:
        print("Queue is empty")


def request_generator():
    while not stop_event.is_set():
        generate_request()
        stop_event.wait(random.uniform(0, 3))

def request_processor():
    while not stop_event.is_set():
        process_request()
        if queue.empty():
            stop_event.wait(0.5)

if __name__ == "__main__":
    print("Welcome to Bank Request Simulator!")
    print("You can exit anytime you want...")
    print("just tap Ctrl + C")
    user_answer = input("Are you ready to start? y / n  ").strip().lower()

    if user_answer != 'y':
        sys.exit()

    new_request_thread = threading.Thread(target=request_generator)
    process_request_thread = threading.Thread(target=request_processor)

    try:
        new_request_thread.start()
        process_request_thread.start()
        while not stop_event.is_set():
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nStopping simulation...")
    finally:
        stop_event.set()
        new_request_thread.join()
        process_request_thread.join()
        print('Bank Request Simulator closed. Have a nice day!')









