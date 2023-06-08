# --------------------------------------------------------------------------
# ⚠️ WARNING - AUTO-GENERATED CODE - DO NOT EDIT ⚠️
# ⚙️ Generated by 'python -m opgen'
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------
# pylint: disable=W0221,W0222,R0901,W0237
# ruff: noqa: N801,E741
# ruff: noqa: D214,D402,D405,D411,D412,D416,D417
# --------------------------------------------------------------------------

from __future__ import annotations

from typing import Optional, Sequence, TypeVar

from onnx.defs import get_schema

from onnxscript.onnx_opset._impl.opset1 import Opset1
from onnxscript.onnx_types import (
    BOOL,
    COMPLEX64,
    COMPLEX128,
    DOUBLE,
    FLOAT,
    FLOAT16,
    INT8,
    INT16,
    INT32,
    INT64,
    STRING,
    UINT8,
    UINT16,
    UINT32,
    UINT64,
)
from onnxscript.values import Op, Opset


class Opset2(Opset1):
    def __new__(cls):
        return Opset.__new__(cls, "", 2)

    T = TypeVar("T", DOUBLE, FLOAT, FLOAT16)

    def GlobalLpPool(self, X: T, *, p: int = 2) -> T:
        r"""[🌐 GlobalLpPool(2)](https://onnx.ai/onnx/operators/onnx__GlobalLpPool.html#globallppool-2 "Online Documentation")


         GlobalLpPool consumes an input tensor X and applies lp pool pooling across
         the values in the same channel. This is equivalent to LpPool with kernel size
         equal to the spatial dimension of input tensor.

        Args:
            X: (differentiable) Input data tensor from the previous operator; dimensions
                for image case are (N x C x H x W), where N is the batch size, C is the
                number of channels, and H and W are the height and the width of the
                data. For non image case, the dimensions are in the form of (N x C x D1
                x D2 ... Dn), where N is the batch size.

            p: p value of the Lp norm used to pool over the input data.
        """

        schema = get_schema("GlobalLpPool", 2, "")
        op = Op(self, "GlobalLpPool", schema)
        return op(*self._prepare_inputs(schema, X), p=p)

    T = TypeVar("T", DOUBLE, FLOAT, FLOAT16)

    def LpPool(
        self,
        X: T,
        *,
        auto_pad: str = "NOTSET",
        kernel_shape: Optional[Sequence[int]] = None,
        p: int = 2,
        pads: Optional[Sequence[int]] = None,
        strides: Optional[Sequence[int]] = None,
    ) -> T:
        r"""[🌐 LpPool(2)](https://onnx.ai/onnx/operators/onnx__LpPool.html#lppool-2 "Online Documentation")


         LpPool consumes an input tensor X and applies Lp pooling across
         the tensor according to kernel sizes, stride sizes, and pad lengths.
         Lp pooling consisting of computing the Lp norm on all values of a subset
         of the input tensor according to the kernel size and downsampling the
         data into the output tensor Y for further processing.

        Args:
            X: Input data tensor from the previous operator; dimensions for image case
                are (N x C x H x W), where N is the batch size, C is the number of
                channels, and H and W are the height and the width of the data. For non
                image case, the dimensions are in the form of (N x C x D1 x D2 ... Dn),
                where N is the batch size.

            auto_pad: auto_pad must be either NOTSET, SAME_UPPER, SAME_LOWER or VALID.
                Where default value is NOTSET, which means explicit padding is used.
                SAME_UPPER or SAME_LOWER mean pad the input so that the output spatial
                size match the input.In case of odd number add the extra padding at the
                end for SAME_UPPER and at the beginning for SAME_LOWER. VALID mean no
                padding.

            kernel_shape: The size of the kernel along each axis.

            p: p value of the Lp norm used to pool over the input data.

            pads: Padding for the beginning and ending along each spatial axis, it can
                take any value greater than or equal to 0. The value represent the
                number of pixels added to the beginning and end part of the
                corresponding axis. `pads` format should be as follow [x1_begin,
                x2_begin...x1_end, x2_end,...], where xi_begin the number of pixels
                added at the beginning of axis `i` and xi_end, the number of pixels
                added at the end of axis `i`. This attribute cannot be used
                simultaneously with auto_pad attribute. If not present, the padding
                defaults to 0 along start and end of each spatial axis.

            strides: Stride along each spatial axis.
        """

        schema = get_schema("LpPool", 2, "")
        op = Op(self, "LpPool", schema)
        return op(
            *self._prepare_inputs(schema, X),
            auto_pad=auto_pad,
            kernel_shape=kernel_shape,
            p=p,
            pads=pads,
            strides=strides,
        )

    T = TypeVar("T", DOUBLE, FLOAT, FLOAT16)

    def Pad(
        self,
        data: T,
        *,
        mode: str = "constant",
        pads: Optional[Sequence[int]] = None,
        value: float = 0.0,
    ) -> T:
        r"""[🌐 Pad(2)](https://onnx.ai/onnx/operators/onnx__Pad.html#pad-2 "Online Documentation")


        Given `data` tensor, pads, mode, and value.
        Example:
          Insert 0 pads to the beginning of the second dimension.
          data = [
              [1.0, 1.2],
              [2.3, 3.4],
              [4.5, 5.7],
          ]
          pads = [0, 2, 0, 0]
          output = [
              [
                  [0.0, 0.0, 1.0, 1.2],
                  [0.0, 0.0, 2.3, 3.4],
                  [0.0, 0.0, 4.5, 5.7],
              ],
          ]


        Args:
            data: Input tensor.

            mode: Three modes: constant(default), reflect, edge

            pads: List of integers indicating the number of padding elements to add or
                remove (if negative) at the beginning and end of each axis. For 2D it is
                the number of pixels. `pads` rank should be double of the input's rank.
                `pads` format should be as follow [x1_begin, x2_begin...x1_end,
                x2_end,...], where xi_begin the number of pixels added at the beginning
                of axis `i` and xi_end, the number of pixels added at the end of axis
                `i`.

            value: One float, indicates the value to be filled.
        """

        schema = get_schema("Pad", 2, "")
        op = Op(self, "Pad", schema)
        return op(*self._prepare_inputs(schema, data), mode=mode, pads=pads, value=value)

    T = TypeVar(
        "T",
        BOOL,
        COMPLEX128,
        COMPLEX64,
        DOUBLE,
        FLOAT,
        FLOAT16,
        INT16,
        INT32,
        INT64,
        INT8,
        STRING,
        UINT16,
        UINT32,
        UINT64,
        UINT8,
    )

    def Split(self, input: T, *, axis: int = 0, split: Optional[Sequence[int]] = None) -> T:
        r"""[🌐 Split(2)](https://onnx.ai/onnx/operators/onnx__Split.html#split-2 "Online Documentation")

        Split a tensor into a list of tensors, along the specified
        'axis'. Lengths of the parts can be specified using argument 'split'.
        Otherwise, the tensor is split to equal sized parts.


        Args:
            input: The tensor to split

            axis: Which axis to split on.

            split: length of each output
        """

        schema = get_schema("Split", 2, "")
        op = Op(self, "Split", schema)
        return op(*self._prepare_inputs(schema, input), axis=axis, split=split)
