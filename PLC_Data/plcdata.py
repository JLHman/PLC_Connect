from flask import Flask, jsonify,Blueprint, flash, g, redirect, render_template, request, session, url_for
from pylogix import PLC

from PLC_Data.auth import login_required
from PLC_Data.db import get_db

bp = Blueprint('plcdata', __name__,url_prefix='/')




@bp.route('/pylogix/v1.0/plc/<ipAddress>/<int:slot>/tags', methods=['GET'])
@login_required
def get_all_tags(ipAddress, slot):
    tags = []

    comm = PLC(ipAddress, slot)
    ret = comm.GetTagList()
    comm.Close()

    if ret.Value is None:
        return jsonify(ret.Status)

    for tag in ret.Value:
        tags.append(
            {"tagName": tag.TagName,
             "dataType": tag.DataType
             })

    return jsonify({'tags': tags})



