import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import arcade
from insightface.app import FaceAnalysis
face = []
class FaceIdentification:
    def __init__(self, model_name):
        self.app = FaceAnalysis(name=model_name, providers=["CUDAExecutionProvider", "CPUExecutionProvider"])
        self.app.prepare(ctx_id=0, det_size=(640, 640))

    def creat_face_bank(app,face_bank_path):
        face_bank_path = face_bank_path
        face_bank = []
        for person_name in os.listdir(face_bank_path):
            file_path = os.path.join(face_bank_path,person_name)
            if os.path.isdir(file_path):
                for image_name in os.listdir(file_path):
                    if image_name != ".DS_Store":
                        image_path = os.path.join(file_path,image_name)
                        image  = cv2.imread(image_path)
                        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
                        result = app.get(image)
                        if len(result) > 1:
                            print("no")
                            continue
                        embedding = result[0]["embedding"]
                        my_dict = {"name":person_name , "embedding":embedding}
                        face_bank.append(my_dict)
        print(face_bank)
        np.save("face_bank.npy", face_bank)  

    def draw_bounding_box(results,input_image,face_bank):
        for result in results:
            cv2.rectangle(input_image,(int(result.bbox[0]),int(result.bbox[1])),(int(result.bbox[2]),int(result.bbox[3])),(0,255,0),2)
            for person in face_bank:
                face_bank_person_embedding = person["embedding"]
                new_person_embedding = result["embedding"]
                distance = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding) **2))
                if distance < 25:
                    cv2.putText(input_image,person["name"],
                    (int(result.bbox[0])-50 , int(result.bbox[1])-10),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(255,255,255),2,cv2.LINE_AA)
                    print(person["embedding"])
                    print(face)
                    break
            else:
                cv2.putText(input_image,"Unknown",
                    (int(result.bbox[0])-50 , int(result.bbox[1])-10),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2,cv2.LINE_AA)
        return input_image
    def draw_bounding_box_name(results,input_image,face_bank):
        for result in results:
            cv2.rectangle(input_image,(int(result.bbox[0]),int(result.bbox[1])),(int(result.bbox[2]),int(result.bbox[3])),(0,255,0),2)
            for person in face_bank:
                face_bank_person_embedding = person["embedding"]
                new_person_embedding = result["embedding"]
                distance = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding) **2))
                if distance < 25:
                    face.append(person["name"])
                    print(face)
                    break
            else:
                print("Unknown")
        return face

            
    # def face_id(results,input_image,face_bank):
    #     for result in results:
    #         cv2.rectangle(input_image,(int(result.bbox[0]),int(result.bbox[1])),(int(result.bbox[2]),int(result.bbox[3])),(0,255,0),2)
    #         for person in face_bank:
    #             face_bank_person_embedding = person["embedding"]
    #             new_person_embedding = result["embedding"]
    #             distance = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding) **2))
    #             if distance < 25:
    #                 cv2.putText(input_image,person["name"],
    #                 (int(result.bbox[0])-50 , int(result.bbox[1])-10),
    #                 cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),2,cv2.LINE_AA)
    #                 print("ok welcome to game pong")
    #                 game = Game()
    #                 arcade.run()
    #                 break
    #         else:
    #                 text = False
    #                 # break
    #         return text