# Aokana-Extractor
Extract data from Aokana(蒼の彼方のフォーリズム) Steam Version

* PRead.cs -  
  * Reversed C# code from AssemblyCsharp.dll, related to decryption
    
* extract.py -   
  * python3 extract.py <input_file.dat> <output_path>
    * extract data from input_file.dat to output_path
  * python3 extract.py <input_file.dat>
    * display file(s) contained in nput_file.dat
      
* convert.py -   
  * convert group of files from webp format to png(ffmpeg required)
    
* conbine.py - 
  * combine all cg based on vcglist.csv(extracted from system.dat), should put all sprite&cg(include SD, evcg) under same directory


For further detail(Such as CG combination or Download, in Chinese), see [https://zhuanlan.zhihu.com/p/108191499]
