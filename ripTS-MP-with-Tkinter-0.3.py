import urllib
import urllib2
import platform
import subprocess
import time
import re
import traceback
import math
import datetime
from multiprocessing import Value, Lock, Process, Pool
from Tkinter import *
from Tkinter import Tk, BOTH
from ttk import Frame, Button, Style
from urlparse import urlparse, urljoin
from posixpath import basename, dirname
# Multiprocessing
counter = None
global userInputURL
userInputURL = ""
global outputFileName
outputFileName = ""
global chkboxCombine
chkboxCombine = True
global chkboxDelete
chkboxDelete = True
global chkboxEncode
chkboxEncode = False

class MyDialog(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        top = self.top = Toplevel(parent)

        self.parent = parent

        self.initUI()

    def onClick(self):
        global chkboxCombine
        global chkboxDelete
        global chkboxEncode

        if self.var.get() == True:
            chkboxCombine = True
        else:
            chkboxCombine = False

        if self.var2.get() == True:
            chkboxDelete = True
        else:
            chkboxDelete = False

        if self.var3.get() == True:
            chkboxEncode = True
        else:
            chkboxEncode = False

    def okBtn(self, val1,val2):
        global userInputURL
        global outputFileName
        global chkboxCombine
        global chkboxDelete
        global chkboxEncode

        userInputURL = val1
        outputFileName = val2

        print '*** ripTS Settings ***'
        print 'URL of m3u8: ',userInputURL
        print ''

        if (outputFileName == ""):
            print 'No custom output file name detected'
            print 'Default output file name CompleteVideo.ts will be used'
            print ''
        else:
            print "Custom output file name: ", outputFileName
            print ''

        if (chkboxDelete == True and chkboxCombine == False):
            print '[!WARNING!] To have DeleteTS enabled you must have CombineTS enabled [!WARNING!]'
            print ''
            chkboxCombine = True

        print 'Combine TS Files: ',str(chkboxCombine)
        print 'Delete Individual TS files after Combining: ',str(chkboxDelete)
        print 'Encode TS Files to Mpeg: ',str(chkboxEncode)
        print ''

        self.top.destroy()
    def onExit(self):
        self.top.destroy()

    def initUI(self):
        self.parent.title("ripTS")
        self.style = Style()
        self.style.theme_use("default")

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        lbl1 = Label(frame, text=" m38u URL ", width=10)
        lbl1.pack(side=LEFT, padx=10, pady=10, )

        entry1 = Entry(frame)
        entry1.pack(fill=X, padx=8, expand=True)

        frame2 = Frame(self, relief=RAISED, borderwidth=1)
        frame2.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        lbl2 = Label(frame2, text=" Output FileName ", width=15)
        lbl2.pack(side=LEFT, padx=10, pady=10)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=8, expand=True)

        frame3 = Frame(self, relief=RAISED, borderwidth=1)
        frame3.pack(fill=BOTH, expand=True)
        self.pack(fill=BOTH, expand=True)

        self.var = BooleanVar()
        cb = Checkbutton(frame3, text="CombineTS",variable=self.var, command=self.onClick)
        cb.pack(side=LEFT, padx=10, pady=10)
        cb.select() # Default Selected

        self.var2 = BooleanVar()
        cb2 = Checkbutton(frame3, text="DeleteTS", variable=self.var2, command=self.onClick)
        cb2.pack(side=LEFT, padx=10, pady=10)
        cb2.select()  # Default Selected

        self.var3 = BooleanVar()
        cb3 = Checkbutton(frame3, text="EncodeTS", variable=self.var3, command=self.onClick)
        cb3.pack(side=LEFT, padx=10, pady=10)

        closeButton = Button(self, text="Close", command=self.onExit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="OK", command=lambda: self.okBtn(entry1.get(),entry2.get()))
        okButton.pack(side=RIGHT)

def combineTS():
    global linecountRounded
    global outputFileName
    # Combinding Files to form one TS file without using a 3rd party program
    # Windows == copy /b *.ts CompleteVideo.ts
    # Nix == cat *.ts >> CompleteVideo.ts
    OSplatform = platform.system()
    if OSplatform == 'Windows':
        print 'Waiting 3 seconds to ensure all downloads have completed'
        time.sleep(3)
        print 'Merging TS files into one video file'
        # DOS copy does not organize files name correctly so the videos will be out of sync if you dont manually sync them in order
        # Merge 0 - 9
        #subprocess.call('copy /b video-0.ts + video-1.ts + video-2.ts + video-3.ts + video-4.ts + video-5.ts + video-6.ts + video-7.ts + video-8.ts + video-9.ts videoA.ts',shell=True)
        subprocess.call('copy /b video-1.ts + video-2.ts + video-3.ts + video-4.ts + video-5.ts + video-6.ts + video-7.ts + video-8.ts + video-9.ts videoA.ts',shell=True)
        if linecountRounded > 10:
            # Merge 10 - 99
            subprocess.call(
                'copy /b video-10.ts + video-11.ts + video-12.ts + video-13.ts + video-14.ts + video-15.ts + video-16.ts + video-17.ts + video-18.ts + video-19.ts + video-20.ts + video-21.ts + video-22.ts + video-23.ts + video-24.ts + video-25.ts + video-26.ts + video-27.ts + video-28.ts + video-29.ts + video-30.ts + video-31.ts + video-32.ts + video-33.ts + video-34.ts + video-35.ts + video-36.ts + video-37.ts + video-38.ts + video-39.ts + video-40.ts + video-41.ts + video-42.ts + video-43.ts + video-44.ts + video-45.ts + video-46.ts + video-47.ts + video-48.ts + video-49.ts + video-50.ts + video-51.ts + video-52.ts + video-53.ts + video-54.ts + video-55.ts + video-56.ts + video-57.ts + video-58.ts + video-59.ts + video-60.ts + video-61.ts + video-62.ts + video-63.ts + video-64.ts + video-65.ts + video-66.ts + video-67.ts + video-68.ts + video-69.ts + video-70.ts + video-71.ts + video-72.ts + video-73.ts + video-74.ts + video-75.ts + video-76.ts + video-77.ts + video-78.ts + video-79.ts + video-80.ts + video-81.ts + video-82.ts + video-83.ts + video-84.ts + video-85.ts + video-86.ts + video-87.ts + video-88.ts + video-89.ts + video-90.ts + video-91.ts + video-92.ts + video-93.ts + video-94.ts + video-95.ts + video-96.ts + video-97.ts + video-98.ts + video-99.ts videoB.ts',
                shell=True)
            if linecountRounded > 100:
                # Merge 100 - 199
                subprocess.call(
                    'copy /b video-100.ts + video-101.ts + video-102.ts + video-103.ts + video-104.ts + video-105.ts + video-106.ts + video-107.ts + video-108.ts + video-109.ts + video-110.ts + video-111.ts + video-112.ts + video-113.ts + video-114.ts + video-115.ts + video-116.ts + video-117.ts + video-118.ts + video-119.ts + video-120.ts + video-121.ts + video-122.ts + video-123.ts + video-124.ts + video-125.ts + video-126.ts + video-127.ts + video-128.ts + video-129.ts + video-130.ts + video-131.ts + video-132.ts + video-133.ts + video-134.ts + video-135.ts + video-136.ts + video-137.ts + video-138.ts + video-139.ts + video-140.ts + video-141.ts + video-142.ts + video-143.ts + video-144.ts + video-145.ts + video-146.ts + video-147.ts + video-148.ts + video-149.ts + video-150.ts + video-151.ts + video-152.ts + video-153.ts + video-154.ts + video-155.ts + video-156.ts + video-157.ts + video-158.ts + video-159.ts + video-160.ts + video-161.ts + video-162.ts + video-163.ts + video-164.ts + video-165.ts + video-166.ts + video-167.ts + video-168.ts + video-169.ts + video-170.ts + video-171.ts + video-172.ts + video-173.ts + video-174.ts + video-175.ts + video-176.ts + video-177.ts + video-178.ts + video-179.ts + video-180.ts + video-181.ts + video-182.ts + video-183.ts + video-184.ts + video-185.ts + video-186.ts + video-187.ts + video-188.ts + video-189.ts + video-190.ts + video-191.ts + video-192.ts + video-193.ts + video-194.ts + video-195.ts + video-196.ts + video-197.ts + video-198.ts + video-199.ts videoC.ts',
                    shell=True)
                if linecountRounded > 200:
                    # Merge 200 - 299
                    subprocess.call(
                        'copy /b video-200.ts + video-201.ts + video-202.ts + video-203.ts + video-204.ts + video-205.ts + video-206.ts + video-207.ts + video-208.ts + video-209.ts + video-210.ts + video-211.ts + video-212.ts + video-213.ts + video-214.ts + video-215.ts + video-216.ts + video-217.ts + video-218.ts + video-219.ts + video-220.ts + video-221.ts + video-222.ts + video-223.ts + video-224.ts + video-225.ts + video-226.ts + video-227.ts + video-228.ts + video-229.ts + video-230.ts + video-231.ts + video-232.ts + video-233.ts + video-234.ts + video-235.ts + video-236.ts + video-237.ts + video-238.ts + video-239.ts + video-240.ts + video-241.ts + video-242.ts + video-243.ts + video-244.ts + video-245.ts + video-246.ts + video-247.ts + video-248.ts + video-249.ts + video-250.ts + video-251.ts + video-252.ts + video-253.ts + video-254.ts + video-255.ts + video-256.ts + video-257.ts + video-258.ts + video-259.ts + video-260.ts + video-261.ts + video-262.ts + video-263.ts + video-264.ts + video-265.ts + video-266.ts + video-267.ts + video-268.ts + video-269.ts + video-270.ts + video-271.ts + video-272.ts + video-273.ts + video-274.ts + video-275.ts + video-276.ts + video-277.ts + video-278.ts + video-279.ts + video-280.ts + video-281.ts + video-282.ts + video-283.ts + video-284.ts + video-285.ts + video-286.ts + video-287.ts + video-288.ts + video-289.ts + video-290.ts + video-291.ts + video-292.ts + video-293.ts + video-294.ts + video-295.ts + video-296.ts + video-297.ts + video-298.ts + video-299.ts videoD.ts',
                        shell=True)
                    if linecountRounded > 300:
                        # Merge 300 - 399
                        subprocess.call(
                            'copy /b video-300.ts + video-301.ts + video-302.ts + video-303.ts + video-304.ts + video-305.ts + video-306.ts + video-307.ts + video-308.ts + video-309.ts + video-310.ts + video-311.ts + video-312.ts + video-313.ts + video-314.ts + video-315.ts + video-316.ts + video-317.ts + video-318.ts + video-319.ts + video-320.ts + video-321.ts + video-322.ts + video-323.ts + video-324.ts + video-325.ts + video-326.ts + video-327.ts + video-328.ts + video-329.ts + video-330.ts + video-331.ts + video-332.ts + video-333.ts + video-334.ts + video-335.ts + video-336.ts + video-337.ts + video-338.ts + video-339.ts + video-340.ts + video-341.ts + video-342.ts + video-343.ts + video-344.ts + video-345.ts + video-346.ts + video-347.ts + video-348.ts + video-349.ts + video-350.ts + video-351.ts + video-352.ts + video-353.ts + video-354.ts + video-355.ts + video-356.ts + video-357.ts + video-358.ts + video-359.ts + video-360.ts + video-361.ts + video-362.ts + video-363.ts + video-364.ts + video-365.ts + video-366.ts + video-367.ts + video-368.ts + video-369.ts + video-370.ts + video-371.ts + video-372.ts + video-373.ts + video-374.ts + video-375.ts + video-376.ts + video-377.ts + video-378.ts + video-379.ts + video-380.ts + video-381.ts + video-382.ts + video-383.ts + video-384.ts + video-385.ts + video-386.ts + video-387.ts + video-388.ts + video-389.ts + video-390.ts + video-391.ts + video-392.ts + video-393.ts + video-394.ts + video-395.ts + video-396.ts + video-397.ts + video-398.ts + video-399.ts videoE.ts',
                            shell=True)
                        if linecountRounded > 400:
                            # Merge 400 - 499
                            subprocess.call(
                                'copy /b video-400.ts + video-401.ts + video-402.ts + video-403.ts + video-404.ts + video-405.ts + video-406.ts + video-407.ts + video-408.ts + video-409.ts + video-410.ts + video-411.ts + video-412.ts + video-413.ts + video-414.ts + video-415.ts + video-416.ts + video-417.ts + video-418.ts + video-419.ts + video-420.ts + video-421.ts + video-422.ts + video-423.ts + video-424.ts + video-425.ts + video-426.ts + video-427.ts + video-428.ts + video-429.ts + video-430.ts + video-431.ts + video-432.ts + video-433.ts + video-434.ts + video-435.ts + video-436.ts + video-437.ts + video-438.ts + video-439.ts + video-440.ts + video-441.ts + video-442.ts + video-443.ts + video-444.ts + video-445.ts + video-446.ts + video-447.ts + video-448.ts + video-449.ts + video-450.ts + video-451.ts + video-452.ts + video-453.ts + video-454.ts + video-455.ts + video-456.ts + video-457.ts + video-458.ts + video-459.ts + video-460.ts + video-461.ts + video-462.ts + video-463.ts + video-464.ts + video-465.ts + video-466.ts + video-467.ts + video-468.ts + video-469.ts + video-470.ts + video-471.ts + video-472.ts + video-473.ts + video-474.ts + video-475.ts + video-476.ts + video-477.ts + video-478.ts + video-479.ts + video-480.ts + video-481.ts + video-482.ts + video-483.ts + video-484.ts + video-485.ts + video-486.ts + video-487.ts + video-488.ts + video-489.ts + video-490.ts + video-491.ts + video-492.ts + video-493.ts + video-494.ts + video-495.ts + video-496.ts + video-497.ts + video-498.ts + video-499.ts videoF.ts',
                                shell=True)
                            if linecountRounded > 500:
                                # Merge 500 - 599
                                subprocess.call(
                                    'copy /b video-500.ts + video-501.ts + video-502.ts + video-503.ts + video-504.ts + video-505.ts + video-506.ts + video-507.ts + video-508.ts + video-509.ts + video-510.ts + video-511.ts + video-512.ts + video-513.ts + video-514.ts + video-515.ts + video-516.ts + video-517.ts + video-518.ts + video-519.ts + video-520.ts + video-521.ts + video-522.ts + video-523.ts + video-524.ts + video-525.ts + video-526.ts + video-527.ts + video-528.ts + video-529.ts + video-530.ts + video-531.ts + video-532.ts + video-533.ts + video-534.ts + video-535.ts + video-536.ts + video-537.ts + video-538.ts + video-539.ts + video-540.ts + video-541.ts + video-542.ts + video-543.ts + video-544.ts + video-545.ts + video-546.ts + video-547.ts + video-548.ts + video-549.ts + video-550.ts + video-551.ts + video-552.ts + video-553.ts + video-554.ts + video-555.ts + video-556.ts + video-557.ts + video-558.ts + video-559.ts + video-560.ts + video-561.ts + video-562.ts + video-563.ts + video-564.ts + video-565.ts + video-566.ts + video-567.ts + video-568.ts + video-569.ts + video-570.ts + video-571.ts + video-572.ts + video-573.ts + video-574.ts + video-575.ts + video-576.ts + video-577.ts + video-578.ts + video-579.ts + video-580.ts + video-581.ts + video-582.ts + video-583.ts + video-584.ts + video-585.ts + video-586.ts + video-587.ts + video-588.ts + video-589.ts + video-590.ts + video-591.ts + video-592.ts + video-593.ts + video-594.ts + video-595.ts + video-596.ts + video-597.ts + video-598.ts + video-599.ts videoG.ts',
                                    shell=True)
                                if linecountRounded > 600:
                                    # Merge 600 - 699
                                    subprocess.call(
                                        'copy /b video-600.ts + video-601.ts + video-602.ts + video-603.ts + video-604.ts + video-605.ts + video-606.ts + video-607.ts + video-608.ts + video-609.ts + video-610.ts + video-611.ts + video-612.ts + video-613.ts + video-614.ts + video-615.ts + video-616.ts + video-617.ts + video-618.ts + video-619.ts + video-620.ts + video-621.ts + video-622.ts + video-623.ts + video-624.ts + video-625.ts + video-626.ts + video-627.ts + video-628.ts + video-629.ts + video-630.ts + video-631.ts + video-632.ts + video-633.ts + video-634.ts + video-635.ts + video-636.ts + video-637.ts + video-638.ts + video-639.ts + video-640.ts + video-641.ts + video-642.ts + video-643.ts + video-644.ts + video-645.ts + video-646.ts + video-647.ts + video-648.ts + video-649.ts + video-650.ts + video-651.ts + video-652.ts + video-653.ts + video-654.ts + video-655.ts + video-656.ts + video-657.ts + video-658.ts + video-659.ts + video-660.ts + video-661.ts + video-662.ts + video-663.ts + video-664.ts + video-665.ts + video-666.ts + video-667.ts + video-668.ts + video-669.ts + video-670.ts + video-671.ts + video-672.ts + video-673.ts + video-674.ts + video-675.ts + video-676.ts + video-677.ts + video-678.ts + video-679.ts + video-680.ts + video-681.ts + video-682.ts + video-683.ts + video-684.ts + video-685.ts + video-686.ts + video-687.ts + video-688.ts + video-689.ts + video-690.ts + video-691.ts + video-692.ts + video-693.ts + video-694.ts + video-695.ts + video-696.ts + video-697.ts + video-698.ts + video-699.ts videoH.ts',
                                        shell=True)
                                    if linecountRounded > 700:
                                        # Merge 700 - 799
                                        subprocess.call(
                                            'copy /b video-700.ts + video-701.ts + video-702.ts + video-703.ts + video-704.ts + video-705.ts + video-706.ts + video-707.ts + video-708.ts + video-709.ts + video-710.ts + video-711.ts + video-712.ts + video-713.ts + video-714.ts + video-715.ts + video-716.ts + video-717.ts + video-718.ts + video-719.ts + video-720.ts + video-721.ts + video-722.ts + video-723.ts + video-724.ts + video-725.ts + video-726.ts + video-727.ts + video-728.ts + video-729.ts + video-730.ts + video-731.ts + video-732.ts + video-733.ts + video-734.ts + video-735.ts + video-736.ts + video-737.ts + video-738.ts + video-739.ts + video-740.ts + video-741.ts + video-742.ts + video-743.ts + video-744.ts + video-745.ts + video-746.ts + video-747.ts + video-748.ts + video-749.ts + video-750.ts + video-751.ts + video-752.ts + video-753.ts + video-754.ts + video-755.ts + video-756.ts + video-757.ts + video-758.ts + video-759.ts + video-760.ts + video-761.ts + video-762.ts + video-763.ts + video-764.ts + video-765.ts + video-766.ts + video-767.ts + video-768.ts + video-769.ts + video-770.ts + video-771.ts + video-772.ts + video-773.ts + video-774.ts + video-775.ts + video-776.ts + video-777.ts + video-778.ts + video-779.ts + video-780.ts + video-781.ts + video-782.ts + video-783.ts + video-784.ts + video-785.ts + video-786.ts + video-787.ts + video-788.ts + video-789.ts + video-790.ts + video-791.ts + video-792.ts + video-793.ts + video-794.ts + video-795.ts + video-796.ts + video-797.ts + video-798.ts + video-799.ts videoI.ts',
                                            shell=True)
                                        if linecountRounded > 800:
                                            # Merge 800 - 899
                                            subprocess.call(
                                                'copy /b video-800.ts + video-801.ts + video-802.ts + video-803.ts + video-804.ts + video-805.ts + video-806.ts + video-807.ts + video-808.ts + video-809.ts + video-810.ts + video-811.ts + video-812.ts + video-813.ts + video-814.ts + video-815.ts + video-816.ts + video-817.ts + video-818.ts + video-819.ts + video-820.ts + video-821.ts + video-822.ts + video-823.ts + video-824.ts + video-825.ts + video-826.ts + video-827.ts + video-828.ts + video-829.ts + video-830.ts + video-831.ts + video-832.ts + video-833.ts + video-834.ts + video-835.ts + video-836.ts + video-837.ts + video-838.ts + video-839.ts + video-840.ts + video-841.ts + video-842.ts + video-843.ts + video-844.ts + video-845.ts + video-846.ts + video-847.ts + video-848.ts + video-849.ts + video-850.ts + video-851.ts + video-852.ts + video-853.ts + video-854.ts + video-855.ts + video-856.ts + video-857.ts + video-858.ts + video-859.ts + video-860.ts + video-861.ts + video-862.ts + video-863.ts + video-864.ts + video-865.ts + video-866.ts + video-867.ts + video-868.ts + video-869.ts + video-870.ts + video-871.ts + video-872.ts + video-873.ts + video-874.ts + video-875.ts + video-876.ts + video-877.ts + video-878.ts + video-879.ts + video-880.ts + video-881.ts + video-882.ts + video-883.ts + video-884.ts + video-885.ts + video-886.ts + video-887.ts + video-888.ts + video-889.ts + video-890.ts + video-891.ts + video-892.ts + video-893.ts + video-894.ts + video-895.ts + video-896.ts + video-897.ts + video-898.ts + video-899.ts videoJ.ts',
                                                shell=True)
                                            if linecountRounded > 900:
                                                # Merge 900 - 999
                                                subprocess.call(
                                                    'copy /b video-900.ts + video-901.ts + video-902.ts + video-903.ts + video-904.ts + video-905.ts + video-906.ts + video-907.ts + video-908.ts + video-909.ts + video-910.ts + video-911.ts + video-912.ts + video-913.ts + video-914.ts + video-915.ts + video-916.ts + video-917.ts + video-918.ts + video-919.ts + video-920.ts + video-921.ts + video-922.ts + video-923.ts + video-924.ts + video-925.ts + video-926.ts + video-927.ts + video-928.ts + video-929.ts + video-930.ts + video-931.ts + video-932.ts + video-933.ts + video-934.ts + video-935.ts + video-936.ts + video-937.ts + video-938.ts + video-939.ts + video-940.ts + video-941.ts + video-942.ts + video-943.ts + video-944.ts + video-945.ts + video-946.ts + video-947.ts + video-948.ts + video-949.ts + video-950.ts + video-951.ts + video-952.ts + video-953.ts + video-954.ts + video-955.ts + video-956.ts + video-957.ts + video-958.ts + video-959.ts + video-960.ts + video-961.ts + video-962.ts + video-963.ts + video-964.ts + video-965.ts + video-966.ts + video-967.ts + video-968.ts + video-969.ts + video-970.ts + video-971.ts + video-972.ts + video-973.ts + video-974.ts + video-975.ts + video-976.ts + video-977.ts + video-978.ts + video-979.ts + video-980.ts + video-981.ts + video-982.ts + video-983.ts + video-984.ts + video-985.ts + video-986.ts + video-987.ts + video-988.ts + video-989.ts + video-990.ts + video-991.ts + video-992.ts + video-993.ts + video-994.ts + video-995.ts + video-996.ts + video-997.ts + video-998.ts + video-999.ts videoK.ts',
                                                    shell=True)
                                                if linecountRounded > 1000:
                                                    # Merge 1000 - 1099
                                                    subprocess.call(
                                                        'copy /b video-1000.ts + video-1001.ts + video-1002.ts + video-1003.ts + video-1004.ts + video-1005.ts + video-1006.ts + video-1007.ts + video-1008.ts + video-1009.ts + video-1010.ts + video-1011.ts + video-1012.ts + video-1013.ts + video-1014.ts + video-1015.ts + video-1016.ts + video-1017.ts + video-1018.ts + video-1019.ts + video-1020.ts + video-1021.ts + video-1022.ts + video-1023.ts + video-1024.ts + video-1025.ts + video-1026.ts + video-1027.ts + video-1028.ts + video-1029.ts + video-1030.ts + video-1031.ts + video-1032.ts + video-1033.ts + video-1034.ts + video-1035.ts + video-1036.ts + video-1037.ts + video-1038.ts + video-1039.ts + video-1040.ts + video-1041.ts + video-1042.ts + video-1043.ts + video-1044.ts + video-1045.ts + video-1046.ts + video-1047.ts + video-1048.ts + video-1049.ts + video-1050.ts + video-1051.ts + video-1052.ts + video-1053.ts + video-1054.ts + video-1055.ts + video-1056.ts + video-1057.ts + video-1058.ts + video-1059.ts + video-1060.ts + video-1061.ts + video-1062.ts + video-1063.ts + video-1064.ts + video-1065.ts + video-1066.ts + video-1067.ts + video-1068.ts + video-1069.ts + video-1070.ts + video-1071.ts + video-1072.ts + video-1073.ts + video-1074.ts + video-1075.ts + video-1076.ts + video-1077.ts + video-1078.ts + video-1079.ts + video-1080.ts + video-1081.ts + video-1082.ts + video-1083.ts + video-1084.ts + video-1085.ts + video-1086.ts + video-1087.ts + video-1088.ts + video-1089.ts + video-1090.ts + video-1091.ts + video-1092.ts + video-1093.ts + video-1094.ts + video-1095.ts + video-1096.ts + video-1097.ts + video-1098.ts + video-1099.ts videoL.ts',
                                                        shell=True)
                                                    if linecountRounded > 1100:
                                                        # Merge 1100 - 1199
                                                        subprocess.call(
                                                            'copy /b video-1100.ts + video-1101.ts + video-1102.ts + video-1103.ts + video-1104.ts + video-1105.ts + video-1106.ts + video-1107.ts + video-1108.ts + video-1109.ts + video-1110.ts + video-1111.ts + video-1112.ts + video-1113.ts + video-1114.ts + video-1115.ts + video-1116.ts + video-1117.ts + video-1118.ts + video-1119.ts + video-1120.ts + video-1121.ts + video-1122.ts + video-1123.ts + video-1124.ts + video-1125.ts + video-1126.ts + video-1127.ts + video-1128.ts + video-1129.ts + video-1130.ts + video-1131.ts + video-1132.ts + video-1133.ts + video-1134.ts + video-1135.ts + video-1136.ts + video-1137.ts + video-1138.ts + video-1139.ts + video-1140.ts + video-1141.ts + video-1142.ts + video-1143.ts + video-1144.ts + video-1145.ts + video-1146.ts + video-1147.ts + video-1148.ts + video-1149.ts + video-1150.ts + video-1151.ts + video-1152.ts + video-1153.ts + video-1154.ts + video-1155.ts + video-1156.ts + video-1157.ts + video-1158.ts + video-1159.ts + video-1160.ts + video-1161.ts + video-1162.ts + video-1163.ts + video-1164.ts + video-1165.ts + video-1166.ts + video-1167.ts + video-1168.ts + video-1169.ts + video-1170.ts + video-1171.ts + video-1172.ts + video-1173.ts + video-1174.ts + video-1175.ts + video-1176.ts + video-1177.ts + video-1178.ts + video-1179.ts + video-1180.ts + video-1181.ts + video-1182.ts + video-1183.ts + video-1184.ts + video-1185.ts + video-1186.ts + video-1187.ts + video-1188.ts + video-1189.ts + video-1190.ts + video-1191.ts + video-1192.ts + video-1193.ts + video-1194.ts + video-1195.ts + video-1196.ts + video-1197.ts + video-1198.ts + video-1199.ts videoM.ts',
                                                            shell=True)
                                                        if linecountRounded > 1200:
                                                            # Merge 1200 - 1299
                                                            subprocess.call(
                                                                'copy /b video-1200.ts + video-1201.ts + video-1202.ts + video-1203.ts + video-1204.ts + video-1205.ts + video-1206.ts + video-1207.ts + video-1208.ts + video-1209.ts + video-1210.ts + video-1211.ts + video-1212.ts + video-1213.ts + video-1214.ts + video-1215.ts + video-1216.ts + video-1217.ts + video-1218.ts + video-1219.ts + video-1220.ts + video-1221.ts + video-1222.ts + video-1223.ts + video-1224.ts + video-1225.ts + video-1226.ts + video-1227.ts + video-1228.ts + video-1229.ts + video-1230.ts + video-1231.ts + video-1232.ts + video-1233.ts + video-1234.ts + video-1235.ts + video-1236.ts + video-1237.ts + video-1238.ts + video-1239.ts + video-1240.ts + video-1241.ts + video-1242.ts + video-1243.ts + video-1244.ts + video-1245.ts + video-1246.ts + video-1247.ts + video-1248.ts + video-1249.ts + video-1250.ts + video-1251.ts + video-1252.ts + video-1253.ts + video-1254.ts + video-1255.ts + video-1256.ts + video-1257.ts + video-1258.ts + video-1259.ts + video-1260.ts + video-1261.ts + video-1262.ts + video-1263.ts + video-1264.ts + video-1265.ts + video-1266.ts + video-1267.ts + video-1268.ts + video-1269.ts + video-1270.ts + video-1271.ts + video-1272.ts + video-1273.ts + video-1274.ts + video-1275.ts + video-1276.ts + video-1277.ts + video-1278.ts + video-1279.ts + video-1280.ts + video-1281.ts + video-1282.ts + video-1283.ts + video-1284.ts + video-1285.ts + video-1286.ts + video-1287.ts + video-1288.ts + video-1289.ts + video-1290.ts + video-1291.ts + video-1292.ts + video-1293.ts + video-1294.ts + video-1295.ts + video-1296.ts + video-1297.ts + video-1298.ts + video-1299.ts videoN.ts',
                                                                shell=True)

        # Merge all videos into CompleteVideo.ts
        if (outputFileName == ""):
            subprocess.call('copy /b videoA.ts + videoB.ts + videoC.ts + videoD.ts + videoE.ts + videoF.ts + videoG.ts + videoH.ts + videoI.ts + videoJ.ts + videoK.ts + videoL.ts + videoM.ts + videoN.ts CompleteVideo.ts', shell=True)
        else:
            #subprocess cannot call directly a variable while issuing the command directly so you have to prepare the command
            newcommand = 'copy /b videoA.ts + videoB.ts + videoC.ts + videoD.ts + videoE.ts + videoF.ts + videoG.ts + videoH.ts + videoI.ts + videoJ.ts + videoK.ts + videoL.ts + videoM.ts + videoN.ts ' + outputFileName + '.ts'''
            subprocess.call(newcommand, shell=True)

        if (chkboxDelete == True):
            print 'Deleting individual TS clips in 3 seconds'
            # Delete individual TS clips because they are all merged now
            time.sleep(3)
            subprocess.call('del video*.ts', shell=True)

    elif OSplatform == 'Linux':
        print 'Waiting 3 seconds to ensure all downloads have completed'
        time.sleep(3)
        print 'Merging TS files into one video file and deleting individual files'
        subprocess.call(['cat *.ts >> CompleteVideo.ts'], shell=True)  # <-- Change the command here
        print 'Deleting individual TS clips in 3 seconds'
        # Delete individual TS clips because they are all merged now
        time.sleep(3)
        subprocess.call(['rm video*.ts'], shell=True)
        print 'CompleteVideo.ts Created Enjoy!'
    else:
        print "FutureBuild"
        sys.exit()

def checkTS():
    global downloadlist
    global userInputURL
    global linecountRounded
    linecountRounded = 0
    downloadlist = []

    response = urllib2.urlopen(userInputURL)
    html = response.read()

    # Combining section to calculate the stop number for DOS merging
    # 5 Headers (Starting) and 1 Ending header of m3u8 file equals 6 lines / carriage returns that should not be counted
    # Then divide everything by 2 (because 2 carriage returns per numbered TS file)  to get the number of TS files that will be downloaded
    linecountINT = html.count('\n')  ## returns number of lines based on carriage return
    linecountINT = (linecountINT - 6.00)
    linecountFLOAT = math.ceil(linecountINT / 2)  # round up the return value because it can sometimes be .5
    linecountRounded = int(linecountFLOAT)

    m = re.search('http', html)
    if m is None:
        o = urlparse(userInputURL)
        reconstructURL = 'http://' + o.netloc + dirname(o.path) + '/'
        m = re.findall('(.*.ts)', html)
        for x in m:
            if o.query == "": #Some websites just have the file name E.G. XYZ-00001.ts
                downloadlist.append(reconstructURL + x)
            else: #Some websites include some form of token that is necessary for downloading E.G. http://XYZ.com/seg-1.ts?e=ABC
                downloadlist.append(reconstructURL + x + '?' + o.query)
    else: #Some websites include the entire URL with the TS file inside the m3u8 E.G http://XYZ.com/seg-1.ts
         m = re.findall('(.*.ts)', html)
         downloadlist = m

def dlTS(x):
    global counter
    with counter.get_lock():
        counter.value += 1

    testfile = urllib.URLopener()
    print "Downloading: " + x
    testfile.retrieve(x, "video-" + str(counter.value) + ".ts")  # retrieve files

def start():
    global userInputURL
    global downloadlist

    counter = Value('i', 0)
    try:
        starterTime = datetime.datetime.now()
        checkTS() #Prepares download list and linecount for combining later
        # Multiprocessing section
        counter = Value('i', 0)
        p = Pool(initializer=init, initargs=(counter,), processes=4)
        i = p.map_async(dlTS, downloadlist, chunksize=1) #download all the TS
        i.wait()

        # combine all the TS files then delete the individual files downloaded
        if (chkboxCombine == True):
            combineTS()

        endingTime = datetime.datetime.now()
        delta = endingTime - starterTime
        print 'ripTS was successful Enjoy!'
        print "ripTS took: " ,delta
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

def init(args): #for multiprocessing
    global counter
    counter = args

if __name__ == '__main__':
    root = Tk() # Tk Dialogue
    root.geometry("300x200+300+300")
    popup = MyDialog(root) # Tk Dialogue
    root.wait_window(popup.top) # Tk Dialogue
    m = re.search('.m3u8', userInputURL)
    if m is None:
        print "[!Error!] Bad URL please check your URL for m3u8 file [!Error!]"
    else:
        print "Starting ripTS"
        start()  # Start download and combine TS Files
