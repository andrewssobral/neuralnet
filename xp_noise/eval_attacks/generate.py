
import os
import glob

def main():
  path = os.path.abspath(os.path.curdir)
  with open('eval_attacks_template.jt') as f:
    template = f.read()
  folders = [
      "2019-02-17_20.21.40.8592","2019-02-17_20.21.40.8597",
      "2019-02-17_20.21.42.5107","2019-02-17_20.21.44.6969",
      "2019-02-17_20.21.46.6696","2019-02-17_20.21.48.5930",
      "2019-02-17_20.21.50.6743","2019-02-17_20.21.53.2363",
      "2019-02-17_20.21.54.6993","2019-02-18_03.35.26.8842",
      "2019-02-18_03.58.51.3775","2019-02-18_04.00.20.9943",
      "2019-02-18_04.00.50.0980","2019-02-18_04.03.40.1196",
      "2019-02-18_04.06.23.5764","2019-02-18_04.07.57.0193",
      "2019-02-18_04.08.54.3196","2019-02-18_04.09.31.0842",
      "2019-02-18_11.27.51.8892","2019-02-18_11.27.51.8876",
      "2019-02-18_11.40.42.2028","2019-02-18_11.41.16.5183",
      "2019-02-18_11.42.54.5557","2019-02-18_11.43.48.7812",
      "2019-02-18_11.45.24.7651","2019-02-18_11.45.24.7648",
      "2019-02-18_11.46.25.9741"
  ]
  run = open('run_all.sh', 'w')
  for i, folder in enumerate(folders):
    file = '{}/sub/eval_attacks_{}.jt'.format(path, i)
    with open(file, 'w') as f:
      f.write(template.format(folder=folder))
    run.write("bsub < {}\n".format(file))

if __name__ == '__main__':
  main()
