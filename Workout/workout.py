# Sketch off the program, this is just functional code not a framework GUI.

import sys
#from PyQt6.QtCore import QSize, Qt
#from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget
import os
from datetime import timedelta
import json

userData = {
    
    }

goals = {
    "strength": {
        "description": "Increasing maximal force production.",
        "rep_range": "3-6",
        "sets": "3-5",
        "intensity": "high",
        "rest": "3-5 min",
        "tempo": "Controlled, explosive"
    },
    "power": {
        "description": "Maximizing explosive force production.",
        "rep_range": "1-5",
        "sets": "3-5",
        "intensity": "high",
        "rest": "3-5 min",
        "tempo": "Explosive"
    },
    "hypertrophy": {
        "description": "Increasing muscle size.",
        "rep_range": "6-12",
        "sets": "3-5",
        "intensity": "medium-high",
        "rest": "1-3 min",
        "tempo": "Controlled, explosive concentric"
    },
    "muscular_endurance": {
        "description": "Improving the ability to sustain repeated contractions.",
        "rep_range": "12-20+",
        "sets": "2-4",
        "intensity": "low-medium",
        "rest": "30-90 sec",
        "tempo": "Controlled"
    },
    "cardio": {
        "description": "Improving cardiovascular endurance and heart health.",
        "rep_range": "30-120 seconds",
        "sets": "2-4",
        "intensity": "medium",
        "rest": "15-60 sec",
        "tempo": "Steady or interval-based"
    },
    "mobility": {
        "description": "Improving active range of motion and control.",
        "rep_range": "8-15 or 30-60 sec",
        "sets": "2-4",
        "intensity": "low",
        "rest": "30-60 sec",
        "tempo": "Slow and controlled"
    },
    "flexibility": {
        "description": "Improving passive range of motion.",
        "rep_range": "30-120 sec",
        "sets": "2-4",
        "intensity": "low",
        "rest": "30-60 sec",
        "tempo": "Slow static holds"
    },
    "recovery": {
        "description": "Promoting recovery and reducing fatigue.",
        "rep_range": "12-20",
        "sets": "2-3",
        "intensity": "low",
        "rest": "1-2 min",
        "tempo": "Slow and controlled"
    },
    "skill": {
        "description": "Improving technique and movement efficiency.",
        "rep_range": "3-8",
        "sets": "3-6",
        "intensity": "low-medium",
        "rest": "1-3 min",
        "tempo": "Controlled and precise"
    }
}

muscle_groups = {

    "shoulders": {
        "front": {
            "description": "The front deltoid (anterior deltoid) is responsible for lifting the arm forward.",
            "Primary function": "Shoulder flexion, pressing movements",
            "Recovery": "48–72 hours"
        },
        "middle": {
            "description": "The lateral deltoid raises the arm out to the side and creates shoulder width.",
            "Primary function": "Shoulder abduction",
            "Recovery": "48–72 hours"
        },
        "back": {
            "description": "The rear deltoid (posterior deltoid) pulls the arm backward and stabilizes the shoulder.",
            "Primary function": "Shoulder extension, horizontal pulling",
            "Recovery": "48–72 hours"
        },
        "rotator cuff": {
            "description": "A group of small muscles that stabilize and rotate the shoulder joint.",
            "Primary function": "Joint stabilization, internal and external rotation",
            "Recovery": "24–48 hours"
        },
    },

    "back": {
        "neck": {
            "description": "Muscles supporting head movement and posture.",
            "Primary function": "Neck flexion, extension, rotation",
            "Recovery": "24–48 hours"
        },
        "trapezius": {
            "description": "Large muscle from neck to mid-back involved in shoulder and scapular movement.",
            "Primary function": "Scapular elevation, retraction, stabilization",
            "Recovery": "48–72 hours"
        },
        "upper": {
            "description": "Upper back muscles around the shoulder blades.",
            "Primary function": "Scapular retraction and elevation",
            "Recovery": "48–72 hours"
        },
        "lats": {
            "description": "Latissimus dorsi muscles responsible for back width and pulling strength.",
            "Primary function": "Shoulder adduction and extension",
            "Recovery": "48–72 hours"
        },
        "middle": {
            "description": "Middle back including rhomboids and mid trapezius.",
            "Primary function": "Scapular retraction",
            "Recovery": "48–72 hours"
        },
        "lower": {
            "description": "Lower back muscles (erector spinae) that support the spine.",
            "Primary function": "Spinal extension and stabilization",
            "Recovery": "72–96 hours"
        },
    },

    "chest": {
        "upper": {
            "description": "Upper chest (clavicular head) activated during incline movements.",
            "Primary function": "Shoulder flexion, horizontal adduction",
            "Recovery": "48–72 hours"
        },
        "middle": {
            "description": "Main chest (sternal head) used in most pressing movements.",
            "Primary function": "Horizontal adduction",
            "Recovery": "48–72 hours"
        },
        "lower": {
            "description": "Lower chest emphasized during decline movements.",
            "Primary function": "Shoulder adduction downward",
            "Recovery": "48–72 hours"
        }
    },

    "abs": {
        "description": "Core muscles including rectus abdominis and obliques.",
        "Primary function": "Spinal flexion, rotation, stabilization",
        "Recovery": "24–48 hours"
    },

    "triceps": {
        "description": "Muscles on the back of the upper arm.",
        "Primary function": "Elbow extension (pushing movements)",
        "Recovery": "48–72 hours"
    },

    "biceps": {
        "description": "Muscles on the front of the upper arm.",
        "Primary function": "Elbow flexion and forearm supination",
        "Recovery": "48–72 hours"
    },

    "forearms": {
        "description": "Muscles responsible for grip and wrist movement.",
        "Primary function": "Grip strength, wrist flexion and extension",
        "Recovery": "24–48 hours"
    },

    "wrists": {
        "description": "Joint and surrounding structures enabling hand movement.",
        "Primary function": "Wrist stabilization and movement",
        "Recovery": "24–48 hours"
    },
    
    "hands": {
        "description": "Small muscles responsible for fine motor control and grip.",
        "Primary function": "Grip strength and dexterity",
        "Recovery": "24–48 hours"
    },

    "hips": {
        "glutes": {
            "description": "Primary hip extensors including gluteus maximus, medius, and minimus.",
            "Primary function": "Hip extension, abduction, stabilization",
            "Recovery": "48–96 hours"
        },
        "hip flexors": {
            "description": "Muscles like the iliopsoas that lift the leg.",
            "Primary function": "Hip flexion",
            "Recovery": "24–48 hours"
        },
        "adductors": {
            "description": "Inner thigh muscles that bring the legs together.",
            "Primary function": "Hip adduction, stabilization",
            "Recovery": "48–72 hours"
        },
        "abductors": {
            "description": "Outer hip muscles including glute medius.",
            "Primary function": "Hip abduction, pelvic stability",
            "Recovery": "48–72 hours"
        },
        "deep stabilizers": {
            "description": "Small muscles that stabilize the hip joint.",
            "Primary function": "Joint stabilization and control",
            "Recovery": "24–48 hours"
        }
    },

    "legs": {
        "quadriceps": {
            "description": "Front thigh muscles responsible for knee extension.",
            "Primary function": "Knee extension",
            "Recovery": "48–72 hours"
        },
        "hamstrings": {
            "description": "Back thigh muscles assisting in knee flexion and hip extension.",
            "Primary function": "Knee flexion, assists hip extension",
            "Recovery": "48–72 hours"
        },
        "calves": {
            "gastrocnemius": {
                "description": "Main calf muscle used in explosive movements.",
                "Primary function": "Plantar flexion",
                "Recovery": "24–48 hours"
            },
            "soleus": {
                "description": "Endurance-focused calf muscle.",
                "Primary function": "Plantar flexion (postural)",
                "Recovery": "24–48 hours"
            }
        },
        "tibialis anterior": {
            "description": "Shin muscle that lifts the foot upward.",
            "Primary function": "Dorsiflexion",
            "Recovery": "24–48 hours"
        }
    },

    "joints": {
        "wrists": {
            "Description": "Highly mobile joint prone to overuse; important for load management.",
            "Recovery": "24–48 hours"
        },
        "elbows": {
            "Description": "Hinge joint used in pushing and pulling movements.",
            "Recovery": "24–48 hours"
        },
        "shoulders": {
            "Description": "Ball-and-socket joint with high mobility and injury risk.",
            "Recovery": "48–72 hours"
        },
        "scapulae": {
            "Description": "Shoulder blade movement system critical for pressing and pulling mechanics.",
            "Recovery": "24–48 hours"
        },
        "hips": {
            "Description": "Large ball-and-socket joint responsible for lower body power and stability.",
            "Recovery": "48–72 hours"
        },
        "knees": {
            "Description": "Hinge joint major load in leg movements like squats and running.",
            "Recovery": "48–72 hours"
        },
        "ankles": {
            "Description": "Joint responsible for foot stability and mobility in movement.",
            "Recovery": "24–48 hours"
        },
        "lower back": {
            "Description": "Lumbar spine responsible for supporting load and posture.",
            "Recovery": "72–96 hours"
        },
        "upper back": {
            "Description": "Thoracic spine aiding posture and rotational movement.",
            "Recovery": "48–72 hours"
        },
        "neck": {
            "Description": "Cervical spine supporting head movement and stability.",
            "Recovery": "24–48 hours"
        }
    }
}


exercises = {
    "neck": {
        
    },
    "chest": {

    },
    "back": {

    },
    "biceps": {

    },
    "legs": {

    }
}

def injurySelector():
    #Adds injuries to this box and keeps them. 
    injuries.lower() = []
    if anyInjuries == True:
        amount = int(input("How many injuries do you have? Write in numbers: \n"))

        for i in range(amount):
            print(muscle_groups)
            location = input("Where is your injury located? Select by muscle group:\n").lower().strip()

            print("1-3 is minor: full workout, maybe swap one exercise\n4-6 is moderate: reduce reps/sets, avoid direct load on injury\n7-9 is severe: recovery exercises only for that muscle group\n10 you should not train that area at all")
            userData["injuryIntensity"] = input("Write how severe your injury is from 1-10")




def newUser():
    global userData

    print("Welcome to workout interpreter, please write your information below:")
    userData["name"] = input("What is your name?")
    print(goals)
    userData["goal"] = input("What is your goal?")
    userData["schedule"] = int(input("How many days a week do you plan to work out?"))
    userData["time"] = int(input("How many hours each workout do you want to use?"))
    userData["injuries"] = input("Do you have any injuries?\n Yes or No: ")

    if userData["injuries"].lower() == "yes":
        injurySelector()
    with open("userData.json", "w") as file:
        json.dump(userData, file, indent=4)

def main():
    global userData

    if os.path.exists("userData.json"):
        with open("userData.json", "r") as file:
            userData = json.load(file)
            print("User data:", userData)
    else:
        newUser()
    while True:
        print(f"Welcome {userData["name"]}")
    

main()