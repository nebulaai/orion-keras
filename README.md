# orion-keras

This is a trial project using Keras framework. It takes the build in MNIST dataset as input. 
A simple sequential neural network will be compiled by keras. 
At the end the trained model will evaluate the score on test dataset. 

# How to run AI model on Orion
- Step one: Packup your AI model into a zip by [Orion-Script-Converter](https://github.com/nebulaai/orion-script-converter).
    
    This convertor will analyze the python code (.py) or jupyter notebook (.ipynb) and ask you a few questions to configure the task. 
    After install the Orion-Script-Converter, start the convertor by typing command "convert2or".
    **Note:**
    - Enter your project
    - Type command 'convert2or'
    
        Input parameters according to the prompt:
        
        1.(Required) Project path: 
	    (Press 'Enter' or '.' for the current directory, '..' for the parent directory of the current folder): 
        
        Input the Python3 project path, either relative path or absolute path. 
        'Enter' or '.' represents the current folder(default) and the '..' means the parent folder 
        of the current path.
        
        2.(Required) entry-point file path(executable file path):
        
        Input the name of entry-point file. This path should inside the Project path.
        
        3.Data configuration: 
	        Do you have external data(data stored outside your project database)
	        that needs to be downloaded from a specific uri (y/n)?
	        
        Set data configuration. If 'y', the following two inputs prompt. Otherwise, this step will skip.
        
            External data uri:  
            
            Input the data uri to get your external data
            
            Path to save the downloaded data within your project:
            
            Input the path(inside your project) to save your downloaded external data.  
            
        4.Path for the task results(project output directory):
        
            Your project output directory holds your output files. 
            If you have such a directory in your project, input it here. 
            Otherwise, there will be no output files.
            
        5.A NBAI task will be created and saved in the 'task_files' folder 
           which is a sibling folder of your project. 

-Step two: submit your AI zip file to Orion. Please follow [this procedure](https://www.youtube.com/watch?v=FzFNgC4sL3g)

