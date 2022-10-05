import argparse
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tsv")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--output-name", required=True)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    transcriptions = {}

    with open(args.tsv, "r") as tsv, open(
        os.path.join(args.output_dir, args.output_name + ".ltr"), "w"
    ) as ltr_out, open(
        os.path.join(args.output_dir, args.output_name + ".wrd"), "w"
    ) as wrd_out:
        root = next(tsv).strip()
        for line in tsv:
            line = line.strip()
            dir = os.sep.join(line.split('\t')[0].split(os.sep)[:-1])
            parts = line.split('\t')[0].split(os.sep)
            trans_path = f"{'.'.join(parts[-1].split('.')[:-1])}.txt"
            path = os.path.join(root,dir,trans_path)
            assert os.path.exists(path)
            texts={}
            part = os.path.basename(line).split(".")[0]
            trans = ''
            with open(path, "r") as trans_f:
                for tline in trans_f:
                    #print('rline:',tline)
                    items = tline.strip()
                    if items=='':
                        items=' '
                    trans += items
            print(trans, file=wrd_out)
            print(
                " ".join(list(trans.replace(" ", "|"))) + " |",
                file=ltr_out,
            )


if __name__ == "__main__":
    main()