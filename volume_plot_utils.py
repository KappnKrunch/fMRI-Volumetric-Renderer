def displayVolume(vol, fileName="display.html", brightness=1, threshold=1, theta=0, phi=0, radius=0, fps=1) :
  #expects tensor data in shape [frames, height, depth, width]
  htmlStats = {"INSERT_VOLUME_WIDTH_HERE":vol.shape[3],
             "INSERT_VOLUME_DEPTH_HERE":vol.shape[2],
             "INSERT_VOLUME_HEIGHT_HERE":vol.shape[1],
             "INSERT_FRAME_COUNT_HERE":vol.shape[0],
             "INSERT_FPS_HERE":fps,
             "INSERT_BRIGHTNESS_HERE":brightness,
             "INSERT_THRESHOLD_HERE":threshold,
             "INSERT_RADIUS_HERE":radius,
             "INSERT_THETA_HERE":theta,
             "INSERT_PHI_HERE":phi,
             "INSERT_FRAMES_HERE": (255.0*vol.flatten()/vol.max().item()).round().tolist() }

  htmlTemplate = open("template.html",'r').read()
  htmlTxt = Template(htmlTemplate).safe_substitute(htmlStats)
  open(fileName,'w').write(htmlTxt)
