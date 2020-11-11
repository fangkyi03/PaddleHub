import paddle
import paddlehub as hub

if __name__ == '__main__':
    model = hub.Module(
        name='resnet50_vd_imagenet_ssld',
        label_list=["roses", "tulips", "daisy", "sunflowers", "dandelion"],
        load_checkpoint=None)
    result = model.predict('flower.jpg')
