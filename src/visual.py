# import cv2
import os
#
# from keras.models import load_model
# # f = h5py.File('example_model.h5', 'r')
# # dset = f.get('model_weights')
# # print(dset.keys())
# # for val in dset.values():
# #     if len(val) > 0:
# #         print(val[0])
# # # dset = f['key']
# # # data = np.array(dset[:,:,:])
# # # file = 'test.jpg'
# # # cv2.imwrite(file, data)
# model = load_model('example_model.h5')
#
# print(model.summary())

for root,dirs,files in os.walk('/mnt/c/Users/devon/PycharmProjects/puzzle/train', topdown=True):
    curDir = root[root.rfind('/')+1:]
    if len(curDir) != 4:
        continue
    print(root)
    print(curDir)
    print(dirs)
    # print(files)
    print('----------------')

