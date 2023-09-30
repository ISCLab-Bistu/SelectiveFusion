
class args():

	# training args
	epochs = 2 #"number of training epochs, default is 2"
	batch_size = 4 #"batch size for training, default is 4"

	#MSRS
	# dataset_ir = "E:\dataset\MSRS\MSRS_Train\Inf"
	# dataset_vi = "E:\dataset\MSRS\MSRS_Train\Vis"
	# HEIGHT = 64
	# WIDTH = 64

	#KAIST
	dataset_ir = "E:\dataset/total_lwir"
	dataset_vi = "E:\dataset/total_visible"
	HEIGHT = 256
	WIDTH = 256

	save_fusion_model = "E:/task/fusion\SCFusion\log"
	save_loss_dir = 'E:/task/fusion\SCKFusion\loss'

	image_size = 256 #"size of training images, default is 256 X 256"
	cuda = 1 #"set it to 1 for running on GPU, 0 for CPU"
	seed = 42 #"random seed for training"

	lr = 1e-4 #"learning rate, default is 0.001"
	log_interval = 10 #"number of images after which the training loss is logged, default is 500"
	resume_fusion_model = None
	# nest net model
	resume_onestage = './models/one-stage/onestage.model'
	alpha_list = [100]#700 0
	w_all_list = [[3.0, 3.0]]#[[6.0, 3.0]] [[5.0, 0.5]] [[6.0, 0.5]] [[6.0, 0.5]] [[3.0, 3.0]]

	# fusion_model = './models/rfn_twostage/'

	fusion_model = './log/'#训练时模型存储路径

	path_fusion = 'E:/task/fusion/SKFusion/log/skfusion/'#推理时模型具体存储路径
	fusion_name = 'Final_epoch_2_alpha_900_wir_3.0_wvi_3.0.model'


