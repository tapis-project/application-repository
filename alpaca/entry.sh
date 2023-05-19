#!/bin/bash

cd /app

echo "Setting HUGGINGFACE_HUB_CACHE to $1..."
export HUGGINGFACE_HUB_CACHE=$1

torchrun --nproc_per_node=$2 --master_port=54321 train.py \
    --model_name_or_path "$3" \
    --data_path ./alpaca_data.json \
    --fp16 True \
    --output_dir /TapisOutput \
    --num_train_epochs $4 \
    --per_device_train_batch_size $5 \
    --per_device_eval_batch_size $6 \
    --gradient_accumulation_steps $7 \
    --evaluation_strategy "$8" \
    --save_strategy "$9" \
    --save_steps ${10} \
    --save_total_limit ${11} \
    --learning_rate ${12} \
    --weight_decay ${13} \
    --warmup_ratio ${14} \
    --lr_scheduler_type "${15}" \
    --logging_steps ${16} \
    --fsdp "${17}" \
    --fsdp_transformer_layer_cls_to_wrap 'OPTDecoderLayer' \
